from django.urls import path
from django.urls import re_path
from .android_api import *
from .web_api import *
from .ml_algo import *
app_name = 'classapp'

urlpatterns = [
    re_path('<parameter1>/', get_recent_attention_percentage),

]
