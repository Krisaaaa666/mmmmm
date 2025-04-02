from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm


# aclounts/models.py

class Student(models.Model):
    user = models.CharField('Логин',max_length=100)
    class_name = models.CharField('Класс',max_length=100)
    subject = models.CharField('Предмет',max_length=100)

    def __str__(self):
        return self.user
