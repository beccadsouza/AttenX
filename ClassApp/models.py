from django.db import models
import datetime


# Create your models here.
class ClassAttention(models.Model):
    hash_key = models.CharField(max_length=100)
    time_stamp = datetime.datetime.now()
    gz_attn = models.CharField(max_length=100)
    ps_attn = models.CharField(max_length=100)
    sleep_n = models.CharField(max_length=100)
    ov_attn = models.CharField(max_length=100)
    n_q = models.CharField(max_length=100)
    n_b = models.CharField(max_length=100)
    n_p = models.CharField(max_length=100)
    pos_attn = models.CharField(max_length=100)

    def __str__(self):
        return self.hash_key


class ClassAttentionID(models.Model):
    hash_key = models.CharField(max_length=100)
    session_teacher = models.CharField(max_length=100)
    time_stamp = datetime.datetime.now()
    class_id = models.CharField(max_length=100)


class ClassAttendance(models.Model):
    session_teacher = models.CharField(max_length=100)
    median_attn = models.CharField(max_length=200)
    num_students = models.CharField(max_length=200)

