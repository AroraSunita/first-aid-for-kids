from django import forms
from django.core.exceptions import ValidationError
from django.utils import timezone
from .models import Contact, Booking
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from datetime import datetime

# TIME_CHOICES for the BookingForm
TIME_CHOICES = [
    ('09:00 - 10:00', '09:00 - 10:00'),
    ('10:00 - 11:00', '10:00 - 11:00'),
    ('11:00 - 12:00', '11:00 - 12:00'),
    ('12:00 - 13:00', '12:00 - 13:00'),
    ('13:00 - 14:00', '13:00 - 14:00'),
    ('14:00 - 15:00', '14:00 - 15:00'),
    ('15:00 - 16:00', '15:00 - 16:00'),
    ('16:00 - 17:00', '16:00 - 17:00'),
]

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['name', 'email', 'comment']

    def __init__(self, *args, **kwargs):
        super(ContactForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.template_pack = 'bootstrap5'
        self.helper.add_input(Submit('submit', 'Submit'))

class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ['first_name', 'last_name', 'email', 'date', 'time', 'comment']
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date'}),
            'time': forms.Select(choices=TIME_CHOICES),
        }

    def clean_date(self):
        date = self.cleaned_data.get('date')
        if date < timezone.now().date():
            raise ValidationError("You cannot book a course in the past.")
        return date

    def clean(self):
        cleaned_data = super().clean()
        date = cleaned_data.get("date")
        time = cleaned_data.get("time")

        if date and time:
            if date == timezone.now().date():
                current_time = timezone.now().strftime('%H:%M')
                end_time = time.split(' - ')[1]
                if end_time <= current_time:
                    raise forms.ValidationError("You cannot book a course at a past time.")

            # Check if the time slot is already booked
            if Booking.objects.filter(date=date, time=time).exists():
                raise forms.ValidationError("This time slot is already booked. Please choose a different time.")