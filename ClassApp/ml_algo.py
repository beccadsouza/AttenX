from django.shortcuts import render
from django.http import HttpResponse
import datetime
from ClassApp.pose_detect import getPoseAttention
from ClassApp.gaze_detect import getGazeAttention
from ClassApp.sleep_detect import getSleepNumber
from ClassApp.models import *
import os
import cv2
import face_recognition
from sklearn.externals import joblib
import numpy as np
import random

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

def appInsights():
    # Side of class less attentive
    # Jokes - range of attention
    return 0
