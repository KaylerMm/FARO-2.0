from django import forms
from .models import Appointment

class AppointmentForm(forms.ModelForm):
    class Meta:
        model = Appointment
        fields = ['pet', 'veterinarian', 'date', 'reason']
        widgets = {
            'date': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
        }
        labels = {
            'pet': 'Pet',
            'veterinarian': 'Veterinarian',
            'date': 'Date and Time',
            'reason': 'Reason for Appointment',
        }
        help_texts = {
            'pet': 'Select the pet for the Appointment.',
            'veterinarian': 'Select the veterinarian for the Appointment.',
            'date': 'Select the date and time for the Appointment.',
            'reason': 'Provide a brief reason for the Appointment.',
        }
        error_messages = {
            'pet': {
                'required': 'Please select a pet for the Appointment.',
            },
            'veterinarian': {
                'required': 'Please select a veterinarian for the Appointment.',
            },
            'date': {
                'required': 'Please select a date and time for the Appointment.',
            },
            'reason': {
                'required': 'Please provide a reason for the Appointment.',
            },
        }