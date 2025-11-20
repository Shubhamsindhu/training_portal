from django.urls import path
from .views import get_courses,get_trainers,get_students

urlpatterns = [
    path('courses/',get_courses,name='get_courses'),
     path('trainers/',get_trainers,name='get_trainers'),
     path('students/',get_students,name='get_students'),
]