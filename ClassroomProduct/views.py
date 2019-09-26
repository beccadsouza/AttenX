from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from PIL import Image
import numpy as np
import json
import time
from qr_code.qrcode.utils import QRCodeOptions

@login_required
def dashboard(request):
    return render(request, 'dashboard.html')


def signout(request):
    return render(request, 'registration/logout.html')


def qrcode(request):
    context = dict(key="rebecca", my_options=QRCodeOptions(size='M', border=6, error_correction='L', image_format='png'))
    return render(request, 'home.html', context=context)


@csrf_exempt
def capture(request):
    all_data = request.POST.get('arr')
    width = int(request.POST.get('width'))
    height = int(request.POST.get('height'))
    img = list(json.loads(all_data)['data'].values())
    temp1 = [img[i:i + 3] for i in range(0, len(img), 4)]
    temp2 = [temp1[i:i + width] for i in range(0, len(temp1), width)]
    array = np.array(temp2, dtype=np.uint8)
    new_image = Image.fromarray(array)
    new_image.save('{0}.png'.format(time.asctime(time.gmtime())))

    return HttpResponse('OK')

