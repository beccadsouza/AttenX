from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
import datetime
from ClassApp.pose_detect import getPoseAttention
from ClassApp.gaze_detect import getGazeAttention
from ClassApp.sleep_detect import getSleepNumber
from ClassApp.models import *
import os
import cv2
import face_recognition
from sklearn.externals import joblib
import pandas as pd
import statistics
import numpy as np
import random
from scipy.stats import pearsonr


# static attendance

# Create your views here.
def MakeAttention(frames):
    # frames = []  # list of frames each being a numpy array image
    print(frames[-1])
    gaze_attn = getGazeAttention(frames[-1])
    print("ga", gaze_attn)
    (pose_attn, n_q, n_b, n_p, unattentive_coordinates) = getPoseAttention(frames[-1])
    sleep_n, sleep_coordinates = getSleepNumber(frames)

    #ov_attn = (gaze_attn+pose_attn)/2 - 0.1*sleep_n
              # + random.randrange(60, 70)

    predictor_model = joblib.load('ClassApp/models/MLP_predictor.pkl')
    ov_attn = predictor_model.predict([[gaze_attn, pose_attn, sleep_n]])[0]
    ov_attn = str(int(ov_attn))
    print(ov_attn)

    session_id = list(ClassAttentionID.objects.all().filter(session_teacher="rebecca"))[-1].hash_key

    image_x = frames[-1].shape[0]
    image_y = frames[-1].shape[1]

    t_l = 0
    b_l = 0
    t_r = 0
    b_r = 0

    for coordinate in unattentive_coordinates:
        if coordinate[0]<(image_x/2) and coordinate[1]<(image_y/2):
            t_l+=1
        elif coordinate[0] < (image_x / 2) and coordinate[1] > (image_y / 2):
            b_l += 1
        if coordinate[0] > (image_x / 2) and coordinate[1] < (image_y / 2):
            t_r += 1
        if coordinate[0] > (image_x / 2) and coordinate[1] > (image_y / 2):
            b_r += 1

    max_value = max(t_l, b_l, t_r, b_r)
    location_text="Top Left"

    if max_value==b_l:
        location_text="Bottom Left"

    elif max_value==t_r:
        location_text="Top Right"

    elif max_value==b_r:
        location_text="Bottom Right"

    obj = ClassAttention(
        hash_key=session_id,gz_attn=str(gaze_attn),ps_attn=str(pose_attn),sleep_n=str(sleep_n),
        ov_attn=str(ov_attn),n_q=str(n_q),n_b=str(n_b),n_p=str(n_p),pos_attn=location_text)
    obj.save()
    # return HttpResponse('tejas')


def DetectAttendance(frames, course, course_time):
    photo=frames[0] # numpy array
    faces=[]
    cv2.imwrite("ClassApp/attendance_students/unknown.jpg",photo)
    for img_name in os.listdir("ClassApp/attendance_students"):
        known_image = face_recognition.load_image_file("ClassApp/attendance_students/"+img_name)
        biden_encoding = face_recognition.face_encodings(known_image)[0]
        faces.append(biden_encoding)

    unknown_image = face_recognition.load_image_file("ClassApp/attendance_students/unknown.jpg")
    unknown_encoding = face_recognition.face_encodings(unknown_image)[0]
    results = face_recognition.compare_faces(faces, unknown_encoding)

    for i,result in enumerate(results):
        if result:
            student_name=os.listdir("ClassApp/attendance_students")[i]
            obj = ClassAttendance(course=str(course), course_time=str(course_time), student_name=student_name)
            obj.save()
            return HttpResponse('tc')

    return HttpResponse("NA")


def StartAttendance(frame):
    face_cascade = cv2.CascadeClassifier('ClassApp/models/haarcascade_frontalface_default.xml')
    all_roi_faces = []
    image = frame
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)
    for i, (x, y, w, h) in enumerate(faces):
        roi_color = image[y:y + h, x:x + w]
        all_roi_faces.append(roi_color)

    faces_enc = []
    for img_name in os.listdir("ClassApp/attendance_students"):
        known_image = face_recognition.load_image_file("ClassApp/attendance_students/" + img_name)
        biden_encoding = face_recognition.face_encodings(known_image)[0]
        faces_enc.append(biden_encoding)

    face_names=[]
    for face_img in all_roi_faces:
        cv2.imwrite("ClassApp/attendance_students/unknown.jpg", face_img)
        unknown_image = face_recognition.load_image_file("ClassApp/attendance_students/unknown.jpg")
        unknown_encoding = face_recognition.face_encodings(unknown_image)[0]
        results = face_recognition.compare_faces(faces_enc, unknown_encoding)
        for i, result in enumerate(results):
            if result:
                student_name = os.listdir("ClassApp/attendance_students")[i]
                face_names.append(student_name)

    # pd.DataFrame(face_names).to_excel('ClassApp/attendance_records/output.xlsx', header=False, index=False)
    hk = ClassAttentionID.objects.last()
    attn = ClassAttention.objects.filter(hash_key=hk).values_list('ov_attn', flat=True)
    print(face_names)
    obj = ClassAttendance(median_attn=np.median(np.array(attn)), num_students=str(len(face_names)))
    obj.save()


def appInsights():
    # Side of class less attentive
    # Jokes - range of attention
    return 0

def relation_output(request):
    attention_ids = ClassAttentionID.objects.filter(session_teacher=request.user)
    np_data=[]
    nb_data=[]
    nq_data=[]
    attns_data=[]

    for attention_id in attention_ids:
        query = ClassAttention.objects.filter(hash_key=attention_id.hash_key)
        sum_np=0
        sum_nb=0
        sum_nq=0
        attns=[]
        for obj in query:
            sum_np += obj.n_p
            sum_nb += obj.n_b
            sum_nq += obj.n_q
            attns.append(obj.ov_attn)
        attns_data.append(statistics.median(attns))

        np_data.append(sum_np)
        nq_data.append(sum_nq)
        nb_data.append(sum_nb)

    corr = []
    corr.append(pearsonr(attns_data, np_data))
    corr.append(pearsonr(attns_data, nq_data))
    corr.append(pearsonr(attns_data, nb_data))


    attr = ["Problem Solving", "Question & Answer", "Speaking"]
    val = []

    for i in range(len(corr)):
        if corr[i] < 0:
            val.append("Attention is negatively related to " + attr[i] + "by a factor of " + str(corr[i]))
        elif corr[i] > 0:
            val.append("Attention is positively related to " + attr[i] + "by a factor of " + str(corr[i]))

    x = {}
    x["recommendations"] = val

    return JsonResponse(x)



