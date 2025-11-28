from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

class Department(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    
    def __str__(self):
        return self.name

class Course(models.Model):
    COURSE_TYPES = [
        ('SHS', 'Senior High School'),
        ('MS', 'Minor Seminary'),
    ]
    
    name = models.CharField(max_length=200)
    code = models.CharField(max_length=20, unique=True)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    course_type = models.CharField(max_length=3, choices=COURSE_TYPES)
    duration = models.CharField(max_length=50)
    description = models.TextField()
    
    def __str__(self):
        return f"{self.name} ({self.code})"

class Student(models.Model):
    GENDER_CHOICES = [
        ('M', 'Male'),
        ('F', 'Female'),
    ]
    
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    student_id = models.CharField(max_length=20, unique=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    date_of_birth = models.DateField()
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    address = models.TextField()
    phone_number = models.CharField(max_length=15)
    email = models.EmailField()
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    enrollment_date = models.DateField(auto_now_add=True)
    profile_picture = models.ImageField(upload_to='students/', blank=True, null=True)
    
    def __str__(self):
        return f"{self.first_name} {self.last_name} ({self.student_id})"
    
    def get_absolute_url(self):
        return reverse('student_detail', kwargs={'pk': self.pk})

class Staff(models.Model):
    STAFF_TYPES = [
        ('TEACHER', 'Teacher'),
        ('ADMIN', 'Administrative'),
        ('SUPPORT', 'Support Staff'),
    ]
    
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    staff_id = models.CharField(max_length=20, unique=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    date_of_birth = models.DateField()
    gender = models.CharField(max_length=1, choices=Student.GENDER_CHOICES)
    address = models.TextField()
    phone_number = models.CharField(max_length=15)
    email = models.EmailField()
    staff_type = models.CharField(max_length=10, choices=STAFF_TYPES)
    department = models.ForeignKey(Department, on_delete=models.SET_NULL, null=True, blank=True)
    hire_date = models.DateField(auto_now_add=True)
    profile_picture = models.ImageField(upload_to='staff/', blank=True, null=True)
    
    def __str__(self):
        return f"{self.first_name} {self.last_name} ({self.staff_id})"

class Subject(models.Model):
    name = models.CharField(max_length=200)
    code = models.CharField(max_length=20, unique=True)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    teacher = models.ForeignKey(Staff, on_delete=models.SET_NULL, null=True, blank=True)
    credit_hours = models.IntegerField()
    
    def __str__(self):
        return f"{self.name} ({self.code})"