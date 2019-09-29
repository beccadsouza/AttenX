from django.contrib import admin
from .models import ClassAttentionID, ClassAttendance, ClassAttention


class ClassAttentionAdmin(admin.ModelAdmin):
    list_display = ('time_stamp',)


class ClassAttentionIDAdmin(admin.ModelAdmin):
    list_display = ('time_stamp',)


admin.site.register(ClassAttendance)
admin.site.register(ClassAttention, ClassAttentionAdmin)
admin.site.register(ClassAttentionID, ClassAttentionIDAdmin)
