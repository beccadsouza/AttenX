from django.urls import path
from django.conf.urls import url
from .android_api import *
app_name = 'classapp'

urlpatterns = [
    path('<parameter1>/', get_recent_attention_percentage, name='attentionpercentage'),
]
