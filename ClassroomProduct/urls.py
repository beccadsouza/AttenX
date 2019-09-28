from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf import settings
from django.conf.urls import url, include
from django.conf.urls.static import static
from django.views.generic import RedirectView
from . import views, manipulate_frames

urlpatterns = [
    url(r'admin/', admin.site.urls),
    url(r'classapp/', include('ClassApp.urls')),
    url(r'accounts/', include('django.contrib.auth.urls')),
    url(r'^signout/', views.signout, name='signout'),
    url(r'^home/', views.home, name='home'),

    url(r'^recordattendance/', views.record_attendance, name="recordattendance"),
    url(r'^captureface/', manipulate_frames.capture_face, name="captureface"),

    url(r'^createsession/', views.create_session, name="createsession"),
    url(r'^streamsession/', views.stream_session, name="streamsession"),
    url(r'^qrcodegen/', views.qr_code_session, name="qrcodegen"),
    url(r'^capture/', manipulate_frames.capture_list, name="capture"),
    # url(r"^dummy/", manipulate_frames.dummy, name="dummy"),

    url(r'^', RedirectView.as_view(pattern_name='home', permanent=False)),
]

urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
