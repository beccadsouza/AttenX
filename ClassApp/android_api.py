from django.http import JsonResponse
from ClassApp.models import *


def get_recent_attention_percentage(request, parameter1):
    percent = ClassAttentionID.objects.get(hash_key=parameter1)
    data = {
        "class_id": percent.class_id,
    }

    return JsonResponse(data)


def get_recent_attention_position(request, parameter1):
    data = {
        "position": "top left",
        "corrective_measure": "quit teaching HAHA ask more questions LOL",
    }

    return JsonResponse(data)
