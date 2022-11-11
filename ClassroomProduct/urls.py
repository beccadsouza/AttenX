from django.contrib import admin
admin.autodiscover()
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf import settings
from django.urls import include, re_path
from django.conf.urls.static import static
from django.views.generic import RedirectView
from .views import *
from .manipulate_frames import *
from ClassApp.web_api import *
from ClassApp.android_api import *
from ClassApp.ml_algo import *

urlpatterns = [
    re_path(r'admin/', admin.site.urls),
    re_path(r'classapp/', include('ClassApp.urls')),

    re_path(r'accounts/', include('django.contrib.auth.urls')),
    re_path(r'^signout/', signout, name='signout'),
    re_path(r'^home/', home, name='home'),

    # url(r'^recordattendance/', views.record_attendance, name="recordattendance"),
    # url(r'^captureface/', manipulate_frames.capture_face, name="captureface"),

    re_path(r'^createsession/', create_session, name="createsession"),
    re_path(r'^streamsession/', stream_session, name="streamsession"),
    re_path(r'^qrcodegen/', qr_code_session, name="qrcodegen"),
    re_path(r'^capture/', capture_list, name="capture"),

    # url(r'^client/parameter1/', get_recent_attention_percentage, name="clientaattention"),


    # url(r'^sessionanalytics/(?P<parameter1>\w+)/', get_session_analytics, name="sessionanalytics"),
    re_path(r'^sessionanalytics/', get_session_analytics, name="sessionanalytics"),
    re_path(r'^sessionlist/', get_list_session, name="sessionlist"),
    re_path(r'^graph/chart1/', chart1,name="chart1"),
    re_path(r'^graph/chart2/',chart2,name="chart2"),
    re_path(r'^graph/chart3/', chart3,name="chart3"),
    re_path(r'^graph/chart4/', chart4,name="chart4"),

    re_path(r"^attendance/", get_attendance, name="attendance"),
    re_path(r'^captureattendance/', capture_attendance,name="captureattendance"),
    re_path(r'^', RedirectView.as_view(pattern_name='home', permanent=False)),

]

urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
