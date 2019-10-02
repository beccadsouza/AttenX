from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf import settings
from django.conf.urls import url, include
from django.conf.urls.static import static
from django.views.generic import RedirectView
from .views import *
from .manipulate_frames import *
from ClassApp.web_api import *
from ClassApp.android_api import *
from ClassApp.ml_algo import *

urlpatterns = [
    url(r'admin/', admin.site.urls),
    url(r'classapp/', include('ClassApp.urls')),

    url(r'accounts/', include('django.contrib.auth.urls')),
    url(r'^signout/', signout, name='signout'),
    url(r'^home/', home, name='home'),

    # url(r'^recordattendance/', views.record_attendance, name="recordattendance"),
    # url(r'^captureface/', manipulate_frames.capture_face, name="captureface"),

    url(r'^createsession/', create_session, name="createsession"),
    url(r'^streamsession/', stream_session, name="streamsession"),
    url(r'^qrcodegen/', qr_code_session, name="qrcodegen"),
    url(r'^capture/', capture_list, name="capture"),

    # url(r'^client/parameter1/', get_recent_attention_percentage, name="clientaattention"),


    # url(r'^sessionanalytics/(?P<parameter1>\w+)/', get_session_analytics, name="sessionanalytics"),
    url(r'^sessionanalytics/', get_session_analytics, name="sessionanalytics"),
    url(r'^sessionlist/', get_list_session, name="sessionlist"),
    url(r'^graph/chart1/', chart1,name="chart1"),
    url(r'^graph/chart2/',chart2,name="chart2"),
    url(r'^graph/chart3/', chart3,name="chart3"),
    url(r'^graph/chart4/', chart4,name="chart4"),

    url(r"^attendance/", get_attendance, name="attendance"),
    url(r'^captureattendance/', capture_attendance,name="captureattendance"),
    url(r'^', RedirectView.as_view(pattern_name='home', permanent=False)),

]

urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
