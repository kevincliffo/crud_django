from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils import timezone

class User(AbstractUser):
    email = models.EmailField(verbose_name='email', max_length=255, unique=True)
    phone = models.CharField(null=True, max_length=255)
    REQUIRED_FIELDS = ['username', 'phone', 'first_name', 'last_name']
    USERNAME_FIELD = 'email'

    def get_username(self):
        return self.email

class Student(models.Model):
    firstname = models.CharField(max_length=100, default="")
    lastname = models.CharField(max_length=100, default="")
    mobile = models.CharField(max_length=100, default="")
    
    def __str__(self):
        return self.firstname + " " + self.lastname

class Exam(models.Model):
    title = models.CharField(max_length=100, default="")
    author = models.CharField(max_length=100, default="")
    content = models.CharField(max_length=100, default="")
    date_added = models.DateTimeField(default=timezone.now)
    
    def __str__(self):
        return self.title
