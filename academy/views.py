from django.shortcuts import render
from .models import Course,Trainer,Student
# Create your views here.
def get_courses(request):
    courses=Course.objects.all()
    context={'courses':courses}
    return render(request,'academy/course_all.html',context)


def get_trainers(request):
    trainers=Trainer.objects.all()
    context={'trainers':trainers}
    return render(request,'academy/trainer_all.html',context)

def get_students(request):
    students=Student.objects.all()
    context={'students':students}
    return render(request,'academy/student_all.html',context)

