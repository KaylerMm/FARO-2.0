from django import forms
from .models import Veterinarian

class VeterinarianForm(forms.ModelForm):
    class Meta:
        model = Veterinarian
        fields = [
            'name',
            'nickname',
            'birth_date',
            'cpf',
            'rg',
            'crmv',
            'specialty',
            'email',
            'phone',
            'phone_2',
            'address',
            'admission_date'
        ]
        widgets = {
            'birth_date': forms.DateInput(attrs={'type': 'date'}),
            'admission_date': forms.DateInput(attrs={'type': 'date'}),
        }
        labels = {
            'name': 'Name',
            'nickname': 'Nickname',
            'birth_date': 'Birth Date',
            'cpf': 'CPF',
            'rg': 'RG',
            'crmv': 'CRMV',
            'specialty': 'Specialty',
            'email': 'Email',
            'phone': 'Phone',
            'phone_2': 'Phone 2',
            'address': 'Address',
            'admission_date': 'Admission Date'
        }
        help_texts = {
            'name': 'Enter the full name of the veterinarian.',
            'nickname': 'Enter the nickname of the veterinarian.',
            'birth_date': 'Enter the birth date of the veterinarian.',
            'cpf': 'Enter the CPF of the veterinarian.',
            'rg': 'Enter the RG of the veterinarian.',
            'crmv': 'Enter the CRMV of the veterinarian.',
            'specialty': 'Enter the specialty of the veterinarian.',
            'email': 'Enter the email address of the veterinarian.',
            'phone': 'Enter the phone number of the veterinarian.',
            'phone_2': 'Enter an alternative phone number of the veterinarian.',
            'address': 'Enter the address of the veterinarian.',
            'admission_date': 'Enter the admission date of the veterinarian.'
        }
        error_messages = {
            'name': {
                'max_length': "This field is too long.",
                'required': "This field is required."
            },
            'cpf': {
                'unique': "This CPF already exists.",
                'required': "This field is required."
            },
            'rg': {
                'unique': "This RG already exists.",
                'required': "This field is required."
            },
            'crmv': {
                'unique': "This CRMV already exists.",
                'required': "This field is required."
            }
        }
