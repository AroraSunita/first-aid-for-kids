from . import views
from django.urls import path

urlpatterns = [
    path('', views.IndexView.as_view(), name='home'),  # Homepage
    path('home/', views.IndexView.as_view(), name='home'),  # Homepage
    path('courses/', views.CoursesView.as_view(), name='courses'),  # Courses page
    path('courses/book/<int:course_id>/', views.BookingView.as_view(), name='book_course'),# Bookings page
    path('booked-courses/', views.UserBookingsView.as_view(), name='booked_courses'),# Booked course page
    path('bookings/edit/<int:booking_id>/', views.EditBookingView.as_view(), name='edit_booking'), # Edit bookings page
    path('bookings/<int:pk>/delete/', views.DeleteBookingView.as_view(), name='delete_booking'),# Delete bookings page
  ]