from django.http import JsonResponse
from ClassApp.models import *
import time


def get_recent_attention_percentage(request, parameter1):
    attention_obj_list = list(ClassAttention.objects.all().filter(hash_key=parameter1))
    attention_id = ClassAttentionID.objects.get(hash_key=parameter1)

    if len(attention_obj_list) == 0:
        data = {
            "time_stamp": time.time(),
            "class_id": attention_id.class_id,
            "session_teacher": attention_id.session_teacher,
            "overall_attention": -1,
            "n_q": 0, #Number of students in Questionning position
            "n_b": 0, #Number of students in Board looking position
            "n_p": 0, #Number of students in Problem Solving  position
            "position": "nothing" #Which part of class in less attentive
        }
    else:
        attention_obj = attention_obj_list[-1]

        data = {
            "time_stamp": attention_obj.time_stamp,
            "class_id": attention_id.class_id,
            "session_teacher": attention_id.session_teacher,
            "overall_attention": attention_obj.ov_attn,
            "n_q": attention_obj.n_q, #Number of students in Questionning position
            "n_b": attention_obj.n_b, #Number of students in Board looking position
            "n_p": attention_obj.n_p, #Number of students in Problem Solving  position
            "position": attention_obj.pos_attn #Which part of class in less attentive
        }

    return JsonResponse(data)

