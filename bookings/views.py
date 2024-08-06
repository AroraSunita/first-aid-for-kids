from django.shortcuts import render, redirect
# from django.views.generic import TemplateView
from django.views.generic import View
from django.contrib import messages
from .forms import ContactForm

class IndexView(View):
    def get(self, request):
        form = ContactForm()
        return render(request, 'bookings/index.html', {'form': form})

    def post(self, request):
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your message has been sent successfully!')
            return redirect('home')
        return render(request, 'bookings/index.html', {'form': form})

# class HomePage(TemplateView):
#     """
#     Displays home page"
#     """
#     template_name = 'base.html' 


