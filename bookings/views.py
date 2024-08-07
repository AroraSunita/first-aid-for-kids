from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import View
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from .forms import ContactForm, BookingForm
from .models import Course, Booking


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
        courses = Course.objects.all()  # Retrieve all course objects from database
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
            messages.success(request, 'Great, you have successfully booked the course!')
            return redirect('home')
        return render(request, 'bookings/booking.html', {'form': form, 'course': course})