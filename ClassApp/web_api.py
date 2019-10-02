from collections import defaultdict
import numpy as np

from django.http import HttpResponse, JsonResponse

from .models import ClassAttention, ClassAttentionID, ClassAttendance


def line_data(request, session_id):
    queryset = ClassAttention.objects.filter(session_id)
    data = []
    for query in queryset:
        temp = {"x": getattr(query, "time_stamp"), "y": getattr(query, "ov_attn")}
        data.append(temp)
    print(data)
    return data


def chart3(request):
    att_id = ClassAttentionID.objects.filter(session_teacher=request.user)
    course_codes = []
    for course in att_id:
        course_codes.append(course.class_id)

    courses = list(set(course_codes))

    course_codes = {}

    for course in courses:
        n = 0
        A = []
        temp = ClassAttentionID.objects.filter(class_id=course)
        for hk in temp:
            timestmps = ClassAttention.objects.filter(hash_key=hk.hash_key)
            for tp in timestmps:
                n += 1
                A.append(int(tp.ov_attn))
        if n != 0:
            course_codes[course] = np.median(A)
    print(course_codes)
    data = {
        "k": list(course_codes.values()),
        "v": list(course_codes.keys()),
    }
    return JsonResponse(data)


def bar_data(request, teacher_id):
    query = ClassAttention.objects.filter(teacher_id)
    timestamp = []
    n_q = [[]]
    n_p = [[]]
    n_b = [[]]
    data = []
    hash_key = " "
    count = -1
    for i in range(len(query)):
        if hash_key == getattr(query[i], "hash_key"):
            n_q[i].append(int(getattr(query[i], "n_q")))
            n_b[i].append(int(getattr(query[i], "n_b")))
            n_q[i].append(int(getattr(query[i], "n_q")))
        else:
            timestamp.append(getattr(query[i], "hash_key").split("_")[2])
            hash_key = getattr(query[i], "hash_key")
            count += 1
            n_q[i].append(int(getattr(query[i], "n_q")))
            n_b[i].append(int(getattr(query[i], "n_b")))
            n_q[i].append(int(getattr(query[i], "n_q")))

    for i in range(len(n_q)):
        fin_nq = [sum(q) / len(q) for q in n_q]
        fin_np = [sum(p) / len(p) for p in n_p]
        fin_nb = [sum(b) / len(b) for b in n_b]
        data = [fin_np, fin_nb, fin_nq, timestamp]
    return data


# def trial(request, parameter1):
#     return JsonResponse({'hk': parameter1})
#

def chart1(request):
    # last six sessions conducted by logged in teacher

    six_sessions = list(ClassAttentionID.objects.filter(session_teacher=request.user))[-6:]

    hash_keys = [x.hash_key for x in six_sessions]

    six_sessions_data = defaultdict(list)

    for hash_key in hash_keys:
        n_q = 0
        n_b = 0
        n_p = 0
        attention = []

        for tmstmp in ClassAttention.objects.filter(hash_key=hash_key):
            n_q += int(tmstmp.n_q)
            n_b += int(tmstmp.n_b)
            n_p += int(tmstmp.n_p)
            attention.append(int(tmstmp.ov_attn))

        six_sessions_data["timestamp"].append(ClassAttentionID.objects.get(hash_key=hash_key).time_stamp)
        six_sessions_data["questions"].append(n_q)
        six_sessions_data["board"].append(n_b)
        six_sessions_data["problem"].append(n_p)
        six_sessions_data["attention"].append(np.median(attention))

    return JsonResponse(six_sessions_data)


def chart2(request):
    session_timestamps = list(ClassAttention.objects.all())[-1]
    session_timestamps_data = defaultdict()

    for tmstmp in session_timestamps_data:
        session_timestamps_data["timestamp"].append(tmstmp.time_stamp)
        session_timestamps_data["attention"].append(tmstmp.ov_attn)

    return JsonResponse(session_timestamps_data)


def chart32(request):
    user_sessions = list(ClassAttentionID.objects.filter(session_teacher=request.user))
    hash_keys = [x.hash_key for x in user_sessions]

    session_class_data = defaultdict()

    for obj in ClassAttention.objects.filter(hash_key__in=hash_keys):
        session_class_data[obj.class_id].append(int(obj.ov_attn))

    final_data = {}

    for k, v in session_class_data.items():
        final_data[k] = np.median(v)

    data = {
        "k": list(final_data.keys()),
        "v": list(final_data.values()),
    }
    return JsonResponse(data)


def chart4(request):
    sessions = ClassAttendance.objects.filter(session_teacher=request.user)
    data_pop = defaultdict(list)

    for x in sessions:
        data_pop[x.num_students].append(x.median_attn)

    data_pop_final = {}

    for k,v in data_pop.items():
        data_pop_final[k] = np.median(v)

    return JsonResponse(data_pop_final)
