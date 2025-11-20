from django.contrib import admin

from .models import Course,Trainer,Student

# Register your models here.


class CourseAdmin(admin.ModelAdmin):
    list_display=['id','course_name','duration']
    list_filter=['course_name']
    search_fields=['id','course_name']
    list_editable=['duration']
    list_display_links=['course_name']
    ordering=['-duration']


class TrainerAdmin(admin.ModelAdmin):
    list_display=['id','full_name']


admin.site.register(Course,CourseAdmin)
admin.site.register(Trainer,TrainerAdmin)
admin.site.register(Student)
