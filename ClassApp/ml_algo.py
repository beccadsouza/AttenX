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

# Create your views here.
def MakeAttention(request):
    frames = [cv2.imread('ClassApp/attendance_students/tejas.jpg'),
              cv2.imread('ClassApp/attendance_students/tejas.jpg'),
              cv2.imread('ClassApp/attendance_students/tejas.jpg'),
              cv2.imread('ClassApp/attendance_students/tejas.jpg'),
              cv2.imread('ClassApp/attendance_students/tejas.jpg')
              ]  # list of frames each being a numpy array image

    gaze_attn = getGazeAttention(frames[-1])
    (pose_attn, n_q, n_b, n_p) = getPoseAttention(frames[-1])
    sleep_n, sleep_coordinates = getSleepNumber(frames)

    ov_attn = (gaze_attn+pose_attn)/2 - 0.1*sleep_n
    print(ov_attn)
    obj = ClassAttention(
        hash_key="1",gz_attn=str(gaze_attn),ps_attn=str(pose_attn),sleep_n=str(sleep_n),
        ov_attn=str(ov_attn),n_q=str(n_q),n_b=str(n_b),n_p=str(n_p),pos_attn="top left")
    obj.save()
    return HttpResponse('tejas')


def DetectAttendance(request):
    photo=cv2.imread('ClassApp/attendance_students/tejas.jpg') # numpy array
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
            obj = ClassAttendance(
                hash_key="1",class_id="1",student_name=student_name)
            obj.save()
            return HttpResponse('tc')

    return HttpResponse("NA")

def appInsights():
    # Side of class less attentive
    # Jokes - range of attention
    return 0
