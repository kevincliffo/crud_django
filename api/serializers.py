
from rest_framework import serializers
from djoser.serializers import UserCreateSerializer, UserSerializer
from . models import Exam, Student, User

class UserCreateSerializer(UserCreateSerializer):
    class Meta(UserCreateSerializer.Meta):
        model = User
        fields = ['id','email','username','password','first_name','last_name','phone']

class ExamsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Exam
        fields = ['id','title','author', 'content','date_added']

class StudentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ['id','firstname','lastname','mobile']