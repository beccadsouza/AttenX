from django.db import models


# Create your models here.
class ClassAttention(models.Model):
    time_stamp = models.CharField(max_length=500)
    gz_attn = models.CharField(max_length=100)
    ps_attn = models.CharField(max_length=100)
    sleep_n = models.CharField(max_length=100)
    ov_attn = models.CharField(max_length=100)
    n_q = models.CharField(max_length=100)
    n_b = models.CharField(max_length=100)
    n_p = models.CharField(max_length=100)

    def __str__(self):
        return self.ov_attn

