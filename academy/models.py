from django.db import models

# Create your models here.

class Course(models.Model):
    course_name = models.CharField(max_length=200)
    description = models.TextField()
    duration = models.IntegerField(help_text="Duration in weeks")
    course_image=models.ImageField(upload_to='images/course_image/')

    def __str__(self):
        return self.course_name

class Trainer(models.Model):
    first_name=models.CharField(max_length=100)
    last_name=models.CharField(max_length=100)
    email=models.EmailField(unique=True,blank=False, null=False)
    l=[
        ('Python','Python'),
        ('Django','Django'),
        ('Data Science','Data Science')
    ]
    expertise=models.CharField(choices=l,default='Python')
    trainer_photo=models.ImageField(upload_to='images/trainer_photo/')


    def full_name(self):
        return f"{self.first_name} {self.last_name}"

    def __str__(self):
        return self.full_name()

class Student(models.Model):
    first_name=models.CharField(max_length=100)
    last_name=models.CharField(max_length=100)
    email=models.EmailField()
    is_active=models.BooleanField(default=False)
    enrolled_course=models.ForeignKey(Course,on_delete=models.SET_NULL,blank=True,null=True)
    trainer=models.ForeignKey(Trainer,on_delete=models.SET_NULL,blank=True,null=True)

    def full_name(self):
        return f"{self.first_name} {self.last_name}"

    def __str__(self):
        return self.full_name()


