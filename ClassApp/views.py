from django.shortcuts import render
import datetime
from .pose_detect import getPoseAttention
from .gaze_detect import getGazeAttention
from .sleep_detect import getSleepNumber
from .models import ClassAttention

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

    # Store id
    return 0


def appInsights():
    # Side of class less attentive
    # Jokes - range of attention
    return 0