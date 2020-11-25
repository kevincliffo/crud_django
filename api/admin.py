from django.contrib import admin
from .models import Exam, User, Student

admin.site.register(Exam)
admin.site.register(Student)
admin.site.register(User)
