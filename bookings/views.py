from django.shortcuts import render, redirect
from django.views.generic import View
from django.contrib import messages
from .forms import ContactForm
from .models import Course

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
        # courses = Course.objects.all()  # Retrieve all course objects from database
        return render(request, 'bookings/course.html')
