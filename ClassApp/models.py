from django.db import models


# Create your models here.
class ClassAttention(models.Model):
    hash_key = models.CharField(max_length=100)
    time_stamp = models.DateTimeField(auto_now_add=True)
    gz_attn = models.CharField(max_length=100)
    ps_attn = models.CharField(max_length=100)
    sleep_n = models.CharField(max_length=100)
    ov_attn = models.CharField(max_length=100)
    n_q = models.CharField(max_length=100)
    n_b = models.CharField(max_length=100)
    n_p = models.CharField(max_length=100)
    pos_attn = models.CharField(max_length=100)

    def __str__(self):
        return self.ov_attn


class ClassAttentionSession(models.Model):
    hash_key = models.CharField(max_length=100)
    session_teacher = models.CharField(max_length=100)
    time_stamp = models.DateField(auto_now_add=True)
    class_id = models.DateTimeField(auto_now_add=True)


class ClassAttendance(models.Model):
    hash_key = models.CharField(max_length=100)
    time_stamp = models.DateTimeField(auto_now_add=True)
    class_id = models.CharField(max_length=1000)
    student_name = models.CharField(max_length=200)

    def __str__(self):
        return self.student_name
