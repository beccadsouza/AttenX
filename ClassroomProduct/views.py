from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from ClassApp.models import *


from qr_code.qrcode.utils import QRCodeOptions


@login_required
def home(request):
    return render(request, 'home.html')


def signout(request):
    return render(request, 'registration/logout.html')


def record_attendance(request):
    return render(request, 'attendance/record_attendance.html')


def create_session(request):
    return render(request, 'attention/create_session.html')


def qr_code_session(request):
    prim_key = ClassAttentionID.objects.all()[0].hash_key
    context = dict(key=prim_key, my_options=QRCodeOptions(size='M', border=6, error_correction='L', image_format='png'))
    return render(request, 'attention/qr_code_session.html', context=context)


def stream_session(request):
    return render(request, 'attention/stream_session.html')




