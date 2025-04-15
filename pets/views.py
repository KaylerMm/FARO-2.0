from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404
from .forms import PetForm
from .models import Pet

@login_required
def pet_list(request):
    query = request.GET.get('q', '')
    if query:
        pets = Pet.objects.filter(name__icontains=query) | Pet.objects.filter(breed__icontains=query) | Pet.objects.filter(color__icontains=query)
    else:
        pets = Pet.objects.all()

    return render(request, 'pets/pet_list.html', {'pets': pets})

@login_required
def create_pet(request):
    if request.method == 'POST':
        form = PetForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('pet_list')
    else:
        form = PetForm()
    return render(request, 'pets/create_pet.html', {'form': form})

@login_required
def edit_pet(request, id):
    pet = get_object_or_404(Pet, id=id)
    if request.method == 'POST':
        form = PetForm(request.POST, instance=pet)
        if form.is_valid():
            form.save()
            return redirect('pet_list')
    else:
        form = PetForm(instance=pet)

    return render(request, 'pets/edit_pet.html', {'form': form, 'pet': pet})

@login_required
def delete_pet(request, id):
    pet = get_object_or_404(Pet, id=id)
    pet.delete()
    return redirect('pet_list')

@login_required
def confirm_delete_pet(request, id):
    pet = get_object_or_404(Pet, id=id)
    
    if request.method == 'POST':
        pet.delete()
        return redirect('pet_list') 
    
    return render(request, 'pets/confirm_delete_pet.html', {'pet': pet})

@login_required

def pet_detail(request, pk):
    pet = get_object_or_404(Pet, pk=pk)
    return render(request, 'pets/pet_detail.html', {'pet': pet})


