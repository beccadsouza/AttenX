from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf import settings
from django.conf.urls import url, include
from django.conf.urls.static import static
from django.views.generic import RedirectView
from . import views, manipulate_frames
from ClassApp.web_api import *
from ClassApp.android_api import *
from ClassApp.ml_algo import *

urlpatterns = [
    url(r'admin/', admin.site.urls),
    # url(r'classapp/', include('ClassApp.urls')),

    url(r'accounts/', include('django.contrib.auth.urls')),
    url(r'^signout/', views.signout, name='signout'),
    url(r'^home/', views.home, name='home'),

    # url(r'^recordattendance/', views.record_attendance, name="recordattendance"),
    # url(r'^captureface/', manipulate_frames.capture_face, name="captureface"),

    url(r'^createsession/', views.create_session, name="createsession"),
    url(r'^streamsession/', views.stream_session, name="streamsession"),
    url(r'^qrcodegen/', views.qr_code_session, name="qrcodegen"),
    url(r'^capture/', manipulate_frames.capture_list, name="capture"),

    url(r'^client/(?P<parameter1>\w+)/', get_recent_attention_percentage, name="clientaattention"),


    url(r'^sessionanalytics/(?P<parameter1>\w+)/', views.get_session_analytics, name="sessionanalytics"),
    url(r'^sessionlist/', views.get_list_session, name="sessionlist"),
    url(r'^graph/donutdata/', donut_data),
    url(r'^graph/trial/(?P<parameter1>\w+)/', trial),

    url(r'^captureattendance/', manipulate_frames.capture_attendance,name="captureattendance"),
    url(r'^', RedirectView.as_view(pattern_name='home', permanent=False)),

]

urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
