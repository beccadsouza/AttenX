from django.shortcuts import render
import datetime
from pose_detect import getPoseAttention
from gaze_detect import getGazeAttention
from sleep_detect import getSleepNumber
from models import ClassAttention
import os
import cv2
import face_recognition

# Create your views here.
def MakeAttention(request):
    frames = []  # list of frames each being a numpy array image

    curr_time = str(datetime.datetime.now().time())

    gaze_attn = getGazeAttention(frames[0])
    (pose_attn,n_q,n_b,n_p) = getPoseAttention(frames[0])
    sleep_n = getSleepNumber(frames)

    ov_attn=(gaze_attn+pose_attn)/2 - 0.1*sleep_n

    obj = ClassAttention.objects.create(curr_time,gaze_attn,pose_attn,sleep_n,ov_attn,n_q,n_b,n_p)
    obj.save()
    return 0


def DetectAttendance(request):
    photo=() # numpy array
    faces=[]
    cv2.imwrite("attendance_students/unknown.jpg",photo)
    for img_name in os.listdir("attendance_students"):
        known_image = face_recognition.load_image_file(img_name)
        biden_encoding = face_recognition.face_encodings(known_image)[0]
        faces.append(biden_encoding)

    unknown_image = face_recognition.load_image_file("attendance_students/unknown.jpg")
    unknown_encoding = face_recognition.face_encodings(unknown_image)[0]
    results = face_recognition.compare_faces(faces, unknown_encoding)

    for i,result in enumerate(results):
        if result:
            student_name=os.listdir("attendance_students")[i]
            #Add model code
    return 0


def appInsights():
    # Side of class less attentive
    # Jokes - range of attention
    return 0
