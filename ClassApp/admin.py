from django.contrib import admin

# Register your models here.

from .models import ClassAttentionID, ClassAttendance, ClassAttention
# Register your models here.
admin.site.register(ClassAttendance)
admin.site.register(ClassAttention)
admin.site.register(ClassAttentionID)