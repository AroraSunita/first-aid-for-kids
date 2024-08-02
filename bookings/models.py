from django.db import models
from django.contrib.auth.models import User
from datetime import datetime

# Create your models here.

class Contact(models.Model):
    name = models.CharField(max_length=200)
    email = models.CharField()
    comment = models.TextField(blank=True)
    date = models.DateField(default=datetime.now, blank=True)
    
    def __str__(self):
        return f"Contact form {self.name}"

class Course(models.Model):
    name = models.CharField(max_length=200)
    description =  models.TextField(max_length=20000, blank=True)

    def __str__(self):
        return self.name

class Booking(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='bookings')
    first_name = models.CharField(max_length=200, blank=True, null=True)
    last_name = models.CharField(max_length=200, blank=True, null=True)
    email = models.CharField()
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    date = models.DateField(default=datetime.now, blank=True)
    time = models.CharField(max_length=200, default= '10:00 - 11:00')
    comment = models.TextField(blank=True)

    def __str__(self):
        return f"{self.user.username} - {self.date} - {self.time}"




