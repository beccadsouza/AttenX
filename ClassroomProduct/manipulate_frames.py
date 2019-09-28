from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render
from django.http import HttpResponse



from ClassApp.ml_algo import *

from PIL import Image
import numpy as np
import json
import time
import ast

# def convert_frame():


# @csrf_exempt
# def get_list_frames(request):
#     data = request.
#
#     return HttpResponse('All OK')


def dummy(request):
    return render(request, 'dummy.html')


@csrf_exempt
def capture_list(request):
    np_frames = []
    list_frames = ast.literal_eval(request.POST.get('list'))
    width = int(request.POST.get('width'))
    height = int(request.POST.get('height'))

    for frame in list_frames:
        img = frame['data'].values()
        temp1 = [img[i:i + 3] for i in range(0, len(img), 4)]
        temp2 = [temp1[i:i + width] for i in range(0, len(temp1), width)]
        np_frame = Image.fromarray(np.array(temp2, dtype=np.uint8))
        np_frames.append(np_frame)

    MakeAttention(np_frames)

    return HttpResponse('OK')
