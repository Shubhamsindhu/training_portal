from django.shortcuts import render, redirect, get_object_or_404
from .models import Course, Trainer, Student
from .forms import CourseForm, StudentForm, TrainerForm
from django.contrib.auth.decorators import permission_required,login_required

# ----------------------------
# Courses
# ----------------------------

def get_courses(request):
    courses = Course.objects.all()
    return render(request, 'academy/course_all.html', {'courses': courses})


def course(request, id):
    course = get_object_or_404(Course, id=id)
    return render(request, 'academy/course_info.html', {'course': course})

@permission_required('academy.add_course', raise_exception=True)
def add_course(request):
    if request.method == 'POST':
        form = CourseForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('get_courses')
    else:
        form = CourseForm()
    return render(request, 'academy/add_course.html', {'form': form})

@permission_required('academy.change_course', raise_exception=True)
def update_course(request, id):
    course = get_object_or_404(Course, id=id)
    if request.method == 'POST':
        form = CourseForm(request.POST, request.FILES, instance=course)
        if form.is_valid():
            form.save()
            return redirect('course', id=id)
    else:
        form = CourseForm(instance=course)
    return render(request, 'academy/update_course.html', {'form': form, 'course': course})

@permission_required('academy.delete_course', raise_exception=True)
def delete_course(request, id):
    course = get_object_or_404(Course, id=id)
    if request.method == 'POST':
        course.delete()
        return redirect('get_courses')
    return render(request, 'academy/delete_course.html', {'course': course})


# ----------------------------
# Trainers
# ----------------------------

def get_trainers(request):
    trainers = Trainer.objects.all()
    return render(request, 'academy/trainer_all.html', {'trainers': trainers})



def trainer(request, id):
    trainer = get_object_or_404(Trainer, id=id)
    return render(request, 'academy/trainer_info.html', {'trainer': trainer})

@permission_required('academy.add_trainer', raise_exception=True)
def add_trainer(request):
    if request.method == 'POST':
        form = TrainerForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('get_trainers')
    else:
        form = TrainerForm()
    return render(request, 'academy/add_trainer.html', {'form': form})

@permission_required('academy.change_trainer', raise_exception=True)
def update_trainer(request, id):
    trainer = get_object_or_404(Trainer, id=id)
    if request.method == 'POST':
        form = TrainerForm(request.POST, request.FILES, instance=trainer)
        if form.is_valid():
            form.save()
            return redirect('trainer', id=id)
    else:
        form = TrainerForm(instance=trainer)
    return render(request, 'academy/update_trainer.html', {'form': form, 'trainer': trainer})

@permission_required('academy.delete_trainer', raise_exception=True)
def delete_trainer(request, id):
    trainer = get_object_or_404(Trainer, id=id)
    if request.method == 'POST':
        trainer.delete()
        return redirect('get_trainers')
    return render(request, 'academy/delete_trainer.html', {'trainer': trainer})


# ----------------------------
# Students
# ----------------------------

def get_students(request):
    students = Student.objects.all()
    return render(request, 'academy/student_all.html', {'students': students})

@login_required
@permission_required('academy.view_student', raise_exception=True)
def student(request, id):
    student_obj = get_object_or_404(Student, id=id)
    # Block normal students from seeing details
    if request.user.groups.filter(name='Student').exists():
        return redirect('get_students')
    return render(request, 'academy/student_info.html', {'student': student_obj})

@permission_required('academy.add_student', raise_exception=True)
def add_student(request):
    if request.method == 'POST':
        form = StudentForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('get_students')
    else:
        form = StudentForm()
    return render(request, 'academy/add_student.html', {'form': form})

@permission_required('academy.change_student', raise_exception=True)
def update_student(request, id):
    student_obj = get_object_or_404(Student, id=id)
    if request.method == 'POST':
        form = StudentForm(request.POST, request.FILES, instance=student_obj)
        if form.is_valid():
            form.save()
            return redirect('student', id=id)
    else:
        form = StudentForm(instance=student_obj)
    return render(request, 'academy/update_student.html', {'form': form, 'student': student_obj})

@permission_required('academy.delete_student', raise_exception=True)
def delete_student(request, id):
    student_obj = get_object_or_404(Student, id=id)
    if request.method == 'POST':
        student_obj.delete()
        return redirect('get_students')
    return render(request, 'academy/delete_student.html', {'student': student_obj})
