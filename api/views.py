from django.shortcuts import render
from .models import Exam, Student
from .serializers import ExamsSerializer, StudentsSerializer
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated

class StudentsViewSet(ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentsSerializer
    permission_classes = (IsAuthenticated,)
    
class ExamsViewSet(ModelViewSet):
    queryset = Exam.objects.all()
    serializer_class = ExamsSerializer