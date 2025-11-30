from django.urls import path
from .views import *

urlpatterns = [
    
     path('trainers/',get_trainers,name='get_trainers'),
    path('trainer/<int:id>/',trainer,name='trainer'),
     path('delete_trainer/<int:id>/',delete_trainer,name='delete_trainer'),
     path('add_trainer/',add_trainer,name='add_trainer'),
     path('update_trainer/<int:id>/',update_trainer,name='update_trainer'),



     path('courses/',get_courses,name='get_courses'),
     path('course/<int:id>/',course,name='course'),
     path('delete_course/<int:id>/',delete_course,name='delete_course'),
     path('add_course/',add_course,name='add_course'),
     path('update_course/<int:id>/',update_course,name='update_course'),

    path('students/',get_students,name='get_students'),
    path('student/<int:id>/', student, name='student'),
    path('add_student/', add_student, name='add_student'),
    path('update_student/<int:id>/', update_student, name='update_student'),
    path('delete_student/<int:id>/', delete_student, name='delete_student'),

]