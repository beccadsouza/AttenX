from django.http import JsonResponse
from ClassApp.models import *


def get_recent_attention_percentage(request, parameter1):
    percent = ClassAttentionID.objects.get(hash_key=parameter1)
    data = {
        "class_id": percent.class_id,
    }

    return JsonResponse(data)
