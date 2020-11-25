from django.shortcuts import render
from .models import Exam, Student
from .serializers import ExamsSerializer, StudentsSerializer
from rest_framework.viewsets import ModelViewSet

class StudentsViewSet(ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentsSerializer

class ExamsViewSet(ModelViewSet):
    queryset = Exam.objects.all()
    serializer_class = ExamsSerializer