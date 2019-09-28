from django.http import JsonResponse
from ClassApp.models import *


def get_recent_attention_percentage(request, parameter1):
    attention_obj = ClassAttentionID.objects.get(hash_key=parameter1)
    data = {
        "class_id": attention_obj.class_id,
        "overall_attention": attention_obj.ov_attn,
        "n_q": attention_obj.n_q, #Number of students in Questionning position
        "n_b": attention_obj.n_b, #Number of students in Board looking position
        "n_p": attention_obj.n_p, #Number of students in Problem Solving  position
        "position": attention_obj.pos_attn #Which part of class in less attentive
    }

    return JsonResponse(data)


def get_recent_attention_position(request, parameter1):
    data = {
        "position": "top left",
        "corrective_measure": "quit teaching HAHA ask more questions LOL",
    }

    return JsonResponse(data)
