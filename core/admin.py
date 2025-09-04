from django.contrib import admin
from .models import School, Student, Teacher

class StudentInline(admin.TabularInline):
    model = Student
    extra = 1 
    show_change_link = True  

class TeacherInline(admin.TabularInline):
    model = Teacher
    extra = 1
    show_change_link = True

@admin.register(School)
class SchoolAdmin(admin.ModelAdmin):
    list_display = ('name', 'address')
    inlines = [StudentInline, TeacherInline]

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('name', 'age', 'grade', 'school')
    list_filter = ('grade', 'school')
    search_fields = ('name',)

@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    list_display = ('name', 'subject', 'school')
    list_filter = ('subject', 'school')
    search_fields = ('name',)
