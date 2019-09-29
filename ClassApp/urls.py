from django.urls import path
from django.conf.urls import url
from .android_api import *
from .web_api import *
from .ml_algo import *
app_name = 'classapp'

urlpatterns = [
    # path('analytics1/', trial),
    path('attendance/', DetectAttendance),
    path('<parameter1>/', get_recent_attention_percentage),

]
