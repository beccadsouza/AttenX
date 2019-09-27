from django.shortcuts import render, redirect
from .models import *
from django.contrib.auth.decorators import login_required
from . import forms


@login_required
def create_class_attention_session(request):
    if request.method == 'POST':
        form = forms.CreateClassAttentionSession(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.session_teacher = request.user
            instance.hash_key = instance.session_teacher+instance.time_stamp+instance.class_id
            instance.save()
            return redirect('home')
    else:
        form = forms.CreateClassAttentionSession()
    return render(request, '', {'form': form})
