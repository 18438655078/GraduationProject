from django.db import models
from django.contrib.auth.models import AbstractUser
# from django import forms

# Create your models here.


class UserInfo(AbstractUser):
    username = models.CharFiled(max_length=60)
    uid = models.AutoField(primary_key=True)
    password = models.CharFiled(max_length=60)
    # telephone = models.CharField(max_length=11, null=True, unique=True)
    # avatar = models.FileField(upload_to='avatars/', default="/avatars/default.png")
    # create_time = models.DateTimeField(verbose_name='创建时间', auto_now_add=True)
    # blog = models.OneToOneField(to='Blog', to_field='nid', null=True)


class OrderInfo(AbstractUser):
    username = models.CharFiled(max_length=60)
    oid = models.AutoField(primary_key=True)
    outkey = models.ForeignKey(UserInfo,on_delete=models.CASCADE,related_name='outkey')
    # password = models.CharFiled(max_length=60)
