from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render
from django.http import HttpResponse
import time


from ClassApp.ml_algo import *

from PIL import Image
import numpy as np
import json
import time
import ast


@csrf_exempt
def capture_list(request):
    np_frames = []
    list_frames = ast.literal_eval(request.POST.get('list'))
    print("Received", len(list_frames), "frames")
    width = int(request.POST.get('width'))
    height = int(request.POST.get('height'))

    for frame in list_frames:
        img = list(frame['data'].values())
        temp1 = [img[i:i + 3] for i in range(0, len(img), 4)]
        temp2 = [temp1[i:i + width] for i in range(0, len(temp1), width)]
        # np_frame = Image.fromarray(np.array(temp2, dtype=np.uint8))
        np_frame = np.array(temp2, dtype=np.uint8)
        np_frames.append(np_frame)
        Image.fromarray(np.array(temp2, dtype=np.uint8)).save("frames/{0}.png".format(time.time()))
    # print("Sending frames to ML Model", len(np_frames))
    MakeAttention(np_frames)

    return HttpResponse('OK')


@csrf_exempt
def capture_attendance(request):
    np_frames = []
    list_frames = ast.literal_eval(request.POST.get('list'))
    print("Received", len(list_frames), "frames")
    width = int(request.POST.get('width'))
    height = int(request.POST.get('height'))

    for frame in list_frames:
        img = list(frame['data'].values())
        temp1 = [img[i:i + 3] for i in range(0, len(img), 4)]
        temp2 = [temp1[i:i + width] for i in range(0, len(temp1), width)]
        # np_frame = Image.fromarray(np.array(temp2, dtype=np.uint8))
        np_frame = np.array(temp2, dtype=np.uint8)
        np_frames.append(np_frame)
        Image.fromarray(np.array(temp2, dtype=np.uint8)).save("frames/Attendance {0}.png".format(time.time()))
    # MakeAttention(np_frames)
    StartAttendance(np_frames[0])

    return HttpResponse('OK')

# @csrf_exempt
# def capture_face(request):
#     np_frames = []
#     list_frames = ast.literal_eval(request.POST.get('list'))
#     print("Received", len(list_frames), "frames")
#     width = int(request.POST.get('width'))
#     height = int(request.POST.get('height'))
#     course_time = request.POST.get('time')
#     course = request.POST.get("course")
#
#     for frame in list_frames:
#         img = list(frame['data'].values())
#         temp1 = [img[i:i + 3] for i in range(0, len(img), 4)]
#         temp2 = [temp1[i:i + width] for i in range(0, len(temp1), width)]
#         # np_frame = Image.fromarray(np.array(temp2, dtype=np.uint8))
#         np_frame = np.array(temp2, dtype=np.uint8)
#         np_frames.append(np_frame)
#         Image.fromarray(np.array(temp2, dtype=np.uint8)).save("Attendance {0}.png".format(time.time()))
#     # MakeAttention(np_frames)
#     DetectAttendance(np_frames, course, course_time)
#
#     return HttpResponse('OK')
