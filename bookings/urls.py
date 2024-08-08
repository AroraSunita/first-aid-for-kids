from . import views
from django.urls import path

urlpatterns = [
    path('', views.IndexView.as_view(), name='home'),  # Homepage
    path('home/', views.IndexView.as_view(), name='home'),  # Homepage
    path('courses/', views.CoursesView.as_view(), name='courses'),  # Courses page
    path('courses/book/<int:course_id>/', views.BookingView.as_view(), name='book_course'),# Bookings page
    path('booked-courses/', views.UserBookingsView.as_view(), name='booked_courses'),# Booked course page
    
  ]