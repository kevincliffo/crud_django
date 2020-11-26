from django.urls import path, include
from . import views
from rest_framework import routers

app_name = 'api'

router = routers.DefaultRouter()
router.register('exams', views.ExamsViewSet)
router.register('students', views.StudentsViewSet)

urlpatterns = [ 
    path('', include(router.urls)),
    path('', include('djoser.urls')),
    path('', include('djoser.urls.authtoken')),
]