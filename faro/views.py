from django.shortcuts import render
from django.contrib import messages
from django.shortcuts import redirect
from django.contrib.auth.models import User
from django import forms

def profile(request):
    return render(request, 'profile.html')

# Formulário personalizado
class ProfileForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email']
        labels = {
            'first_name': 'Nome',
            'last_name': 'Sobrenome',
            'email': 'Email',
        }

def edit_profile(request):
    if request.method == 'POST':
        form = ProfileForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, 'Perfil atualizado com sucesso.')
            return redirect('profile')
    else:
        form = ProfileForm(instance=request.user)

    return render(request, 'edit_profile.html', {'form': form})

