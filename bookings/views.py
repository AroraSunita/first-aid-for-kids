from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import View
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.http import JsonResponse
from .forms import ContactForm, BookingForm
from .models import Course, Booking
from datetime import datetime
from django.urls import reverse_lazy

# Function to check booked times for a specific date
def check_booked_times(request):
    date = request.GET.get('date')
    if date:
        booked_times = Booking.objects.filter(date=date).values_list('time', flat=True)
        return JsonResponse({'booked_times': list(booked_times)})
    return JsonResponse({'booked_times': []})


class IndexView(View):
    def get(self, request):
        form = ContactForm()
        return render(request, 'bookings/index.html', {'form': form})

    def post(self, request):
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your message has been sent successfully! I will be in touch!')
            return redirect('home')
        return render(request, 'bookings/index.html', {'form': form})



class CoursesView(View):
    def get(self, request):
        courses = Course.objects.all().order_by('id')  # Retrieve all course objects from database order by id
        return render(request, 'bookings/course.html', {'courses': courses})



@method_decorator(login_required, name='dispatch')
class BookingView(View):
    def get(self, request, course_id):
        course = get_object_or_404(Course, id=course_id)
        form = BookingForm(initial={
            'course': course,
            'email': request.user.email,
            'first_name': request.user.first_name,
            'last_name': request.user.last_name
        })
        return render(request, 'bookings/booking.html', {'form': form, 'course': course})

    def post(self, request, course_id):
        course = get_object_or_404(Course, id=course_id)
        form = BookingForm(request.POST)
        if form.is_valid():
            booking = form.save(commit=False)
            booking.user = request.user
            booking.course = course
            booking.save()
            messages.success(request, f'Great {request.user.username}, you have successfully booked the course!')
            return redirect('booked_courses')
        else:
            # If form is not valid, re-render the form with errors
            return render(request, 'bookings/booking.html', {'form': form, 'course': course})


@method_decorator(login_required, name='dispatch')
class UserBookingsView(View):
    def get(self, request):
        bookings = Booking.objects.filter(user=request.user).order_by('date')
        return render(request, 'bookings/user_bookings.html', {'bookings': bookings})



@method_decorator(login_required, name='dispatch')
class EditBookingView(View):
    def get(self, request, booking_id):
        booking = get_object_or_404(Booking, id=booking_id, user=request.user)
        form = BookingForm(instance=booking)
        return render(request, 'bookings/edit_booking.html', {'form': form, 'booking': booking})

    def post(self, request, booking_id):
        booking = get_object_or_404(Booking, id=booking_id, user=request.user)
        form = BookingForm(request.POST, instance=booking)
        if form.is_valid():
            form.save()
            messages.success(request, f'Successfully edited the course, {request.user.username}!!')
            return redirect('booked_courses')
        return render(request, 'bookings/edit_booking.html', {'form': form, 'booking': booking})



@method_decorator(login_required, name='dispatch')
class DeleteBookingView(View):
    template_name = 'bookings/confirm_delete.html'

    def get(self, request, booking_id):
        booking = get_object_or_404(Booking, id=booking_id, user=request.user)
        return render(request, self.template_name, {'object': booking})

    def post(self, request, booking_id):
        booking = get_object_or_404(Booking, id=booking_id, user=request.user)
        booking.delete()
        messages.success(request, f'The course has been deleted successfully, {request.user.username}!')
        return redirect('booked_courses')