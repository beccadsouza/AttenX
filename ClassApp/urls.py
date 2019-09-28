from django.urls import path
from django.conf.urls import url
from .android_api import *
from .ml_algo import *
app_name = 'classapp'

urlpatterns = [
    path('tejas/', MakeAttention),
    path('<parameter1>/', get_recent_attention_percentage),
]
