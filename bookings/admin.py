from django.contrib import admin
from .models import Contact, Course, Booking
from django_summernote.admin import SummernoteModelAdmin

# Register your models here.
@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('comment', 'date')
 
@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')
    
@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = ('user', 'first_name', 'last_name', 'email', 'course', 'date', 'time')
    search_fields = ('user__username', 'course__name', 'email')
    list_filter = ('date', 'course')
    
