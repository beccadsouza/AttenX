# from django.shortcuts import render, redirect
# from .models import *
# from django.contrib.auth.decorators import login_required
# from . import forms
# import hashlib
#
#
# @login_required
# def create_class_attention_session(request):
#     if request.method == 'POST':
#         form = forms.CreateClassAttentionSession(request.POST)
#         if form.is_valid():
#             instance = form.save(commit=False)
#             instance.session_teacher = request.user
#             instance.hash_key = hashlib.md5(str(instance.session_teacher+instance.time_stamp+instance.class_id).encode())
#             instance.save()
#             return redirect('qrcodegen')
#     else:
#         form = forms.CreateClassAttentionSession()
#     return render(request, 'attention/create_session.html', {'form': form})
