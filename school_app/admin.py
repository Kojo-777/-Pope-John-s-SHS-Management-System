from django.contrib import admin
from .models import Department, Course, Student, Staff, Subject

@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
    list_display = ['name', 'description']
    search_fields = ['name']

@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ['name', 'code', 'department', 'course_type', 'duration']
    list_filter = ['department', 'course_type']
    search_fields = ['name', 'code']

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ['student_id', 'first_name', 'last_name', 'course', 'enrollment_date']
    list_filter = ['course', 'gender']
    search_fields = ['first_name', 'last_name', 'student_id']

@admin.register(Staff)
class StaffAdmin(admin.ModelAdmin):
    list_display = ['staff_id', 'first_name', 'last_name', 'staff_type', 'department', 'hire_date']
    list_filter = ['staff_type', 'department']
    search_fields = ['first_name', 'last_name', 'staff_id']

@admin.register(Subject)
class SubjectAdmin(admin.ModelAdmin):
    list_display = ['name', 'code', 'course', 'teacher', 'credit_hours']
    list_filter = ['course']
    search_fields = ['name', 'code']