from django import forms
from . import models


class CreateClassAttentionID(forms.ModelForm):
    class Meta:
        model = models.ClassAttentionID
        fields = ['class_id']
