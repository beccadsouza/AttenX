from django import forms
from . import models


class CreateClassAttentionSession(forms.ModelForm):
    class Meta:
        model = models.ClassAttentionSession
        fields = ['class_id']
