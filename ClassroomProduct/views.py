import json
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
import cv2
import numpy as np


@login_required
def dashboard(request):
    return render(request, 'dashboard.html')


def signout(request):
    return render(request, 'registration/logout.html')


@csrf_exempt
def capture(request):
    all_data = request.POST.get('arr')
    width = int(request.POST.get('width'))
    height = int(request.POST.get('height'))
    img = list(json.loads(all_data)['data'].values())
    temp1 = [img[i:i + 3][::-1] for i in range(0, len(img), 4)]
    temp2 = [temp1[i:i + width] for i in range(0, len(temp1), width)]

    return HttpResponse('OK')

def webcam(request):
    cap = cv2.VideoCapture(0)
    fourcc = cv2.VideoWriter_fourcc(*'XVID')
    out = cv2.VideoWriter('output.avi', fourcc, 20.0, (640, 480))

    while True:
        ret, frame = cap.read()
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        out.write(frame)
        cv2.imshow('frame', gray)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    out.release()
    cv2.destroyAllWindows()

    return HttpResponse('Video Got Recorded')
