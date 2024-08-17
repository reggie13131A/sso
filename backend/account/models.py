from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils import timezone

class CustomUser(AbstractUser):
    class Meta:
        verbose_name = '用户'
        verbose_name_plural = '用户管理表'
    email = models.EmailField(verbose_name="邮箱地址")
    phone_number = models.CharField(max_length=11, verbose_name="手机号码")
    name = models.CharField(max_length=20, verbose_name="真名", default="")
    def __str__(self):
        return self.name  # 确保返回的是字符串类型  否则会报错