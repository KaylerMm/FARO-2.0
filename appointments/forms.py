from django import forms
from .models import Appointment
from .models import MedicalRecord

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
        
class MedicalRecordForm(forms.ModelForm):
    class Meta:
        model = MedicalRecord
        fields = ['description', 'medications']
        widgets = {
            'description': forms.Textarea(attrs={'rows': 4}),
            'medications': forms.Textarea(attrs={'rows': 4}),
        }
        labels = {
            'description': 'Appointment Description',
            'medications': 'Medicine Prescribed',
        }
        help_texts = {
            'description': 'Provide a detailed description of the appointment.',
            'medications': 'List any medications prescribed during the appointment.',
        }
        error_messages = {
            'description': {
                'required': 'Please provide a description of the appointment.',
            },
            'medications': {
                'required': 'Please list any medications prescribed.',
            },
        }
        def __init__(self, *args, **kwargs):
            super(MedicalRecordForm, self).__init__(*args, **kwargs)
            self.fields['description'].label = 'Appointment Description'
            self.fields['medications'].label = 'Medicine Prescribed'