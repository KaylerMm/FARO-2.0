from django import forms
from .models import Customer

class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = '__all__'
        widgets = {
            'phone': forms.TextInput(attrs={'class': 'form-control', 'id': 'phone'}),
            'phone_2': forms.TextInput(attrs={'class': 'form-control', 'id': 'phone2'}),
            'cpf': forms.TextInput(attrs={'class': 'form-control', 'id': 'cpf'}),
            'birth_date': forms.TextInput(attrs={'class': 'form-control', 'id': 'birth_date'}),
        }
