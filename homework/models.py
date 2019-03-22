from captcha.fields import CaptchaField
from django.db import models

# Create your models here.
from django.forms import forms


class User(models.Model):
    username = models.CharField(max_length=18)
    realname = models.CharField(max_length=18)
    password = models.CharField(max_length=18)
    age = models.IntegerField(max_length=8)
    sex = models.CharField(max_length=3)
    telephone = models.IntegerField(max_length=12)
    require = models.CharField(max_length=500)
    img = models.ImageField(upload_to='static/img/img', null=True)
    name = models.CharField(max_length=100, null=True)
    create = models.DateTimeField(auto_now_add=True)
    login = models.DateTimeField(auto_now=True)
    captcha = CaptchaField(error_messages={"invalid": "验证码错误"})


