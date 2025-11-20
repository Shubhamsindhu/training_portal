from django.shortcuts import render
from academy.models import Course,Trainer,Student

def home(request):
    courses_count=Course.objects.all().count()
    trainer_count=Trainer.objects.all().count()
    student_count=Student.objects.all().count()
    context={'courses_count':courses_count,'trainer_count':trainer_count,'student_count':student_count}
    return render(request,'home.html',context=context)