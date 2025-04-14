from django import forms
from .models import Pet

class PetForm(forms.ModelForm):
    class Meta:
        model = Pet
        fields = '__all__'
        widgets = {
            'birth_date': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
        }
        labels = {
            'name': 'Name',
            'nickname': 'Nickname',
            'sepecies': 'Species',
            'breed': 'Breed',
            'color': 'Color',
            'birth_date': 'Birth Date',
            'weight': 'Weight (kg)',
            'height': 'Height (cm)',
            'customer': 'Customer',
        }
        help_texts = {
            'name': 'Enter the name of the pet.',
            'nickname': 'Enter a nickname for the pet (optional).',
            'sepecies': 'Enter the species of the pet (e.g., dog, cat).',
            'breed': 'Enter the breed of the pet.',
            'color': 'Enter the color of the pet.',
            'birth_date': 'Select the birth date of the pet.',
            'weight': 'Enter the weight of the pet in kilograms.',
            'height': 'Enter the height of the pet in centimeters.',
            'customer': 'Select the owner of the pet.',
        }
        error_messages = {
            'name': {
                'required': 'This field is required.',
                'max_length': 'This field cannot exceed 100 characters.',
            },
            'nickname': {
                'max_length': 'This field cannot exceed 100 characters.',
            },
            'sepecies': {
                'max_length': 'This field cannot exceed 100 characters.',
            },
            'breed': {
                'max_length': 'This field cannot exceed 100 characters.',
            },
            'color': {
                'max_length': 'This field cannot exceed 50 characters.',
            },
            'weight': {
                'max_digits': 'This field cannot exceed 5 digits.',
                'decimal_places': 'This field cannot have more than 2 decimal places.',
            },
            'height': {
                'max_digits': 'This field cannot exceed 5 digits.',
                'decimal_places': 'This field cannot have more than 2 decimal places.',
            },
            'customer': {
                'required': 'This field is required.',
            },
        }