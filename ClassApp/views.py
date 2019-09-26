from django.shortcuts import render
from .pose_detect import getPoseAttention
from .gaze_detect import getGazeAttention

# Create your views here.
def MakeAttention(request):
    frames=[] # list of frames each being a numpy array image

    # Eye gaze
    gaze_attn = getGazeAttention(frames[0])
    pose_attn = getPoseAttention(frames[0])

    # Sleepy
    # Add to DB

    # Separate tracking for ==>
    # Answering Qs - Raising hands
    # Staring at board/teacher
    # Solving probs

    return 0

def DetectAttendance(request):
    photo=() # numpy array

    # Store id
    return 0

def appInsights():
    # Side of class less attentive
    # Jokes - range of attention
    return 0