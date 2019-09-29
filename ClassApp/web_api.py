from .models import ClassAttention, ClassAttentionID


def line_data(request, session_id):
    queryset = ClassAttention.objects.filter(session_id)
    data = []
    for query in queryset:
        temp = {"x": getattr(query, "time_stamp"), "y": getattr(query, "ov_attn")}
        data.append(temp)
    print(data)
    return data


def donut_data(request, teacher_id):
    subjects = ClassAttentionID.objects.filter(teacher_id)
    sub_list = {}
    for subject in subjects:
        sub_list[getattr(subject, "hash_key")] = getattr(subject, "class_id")

    queryset = ClassAttention.objects.filter(teacher_id)
    data = []
    datasets = []
    labels = []
    print(data)
    return data


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
        fin_nq = [sum(q)/len(q) for q in n_q]
        fin_np = [sum(p)/len(p) for p in n_p]
        fin_nb = [sum(b)/len(b) for b in n_b]
        data = [fin_np, fin_nb, fin_nq, timestamp]
    return data

