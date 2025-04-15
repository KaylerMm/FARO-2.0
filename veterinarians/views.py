from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Veterinarian
from .forms import VeterinarianForm

@login_required
def veterinarian_list(request):
    vets = Veterinarian.objects.all()
    return render(request, 'veterinarians/veterinarian_list.html', {'vets': vets})

@login_required
def create_veterinarian(request):
    form = VeterinarianForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('veterinarian_list')
    return render(request, 'veterinarians/veterinarian_form.html', {'form': form})

@login_required
def update_veterinarian(request, pk):
    vet = get_object_or_404(Veterinarian, pk=pk)
    form = VeterinarianForm(request.POST or None, instance=vet)
    if form.is_valid():
        form.save()
        return redirect('veterinarian_list')
    return render(request, 'veterinarians/veterinarian_form.html', {'form': form})

@login_required
def delete_veterinarian(request, pk):
    vet = get_object_or_404(Veterinarian, pk=pk)
    if request.method == 'POST':
        vet.delete()
        return redirect('veterinarian_list')
    return render(request, 'veterinarians/veterinarian_confirm_delete.html', {'vet': vet})

@login_required
def veterinarian_detail(request, pk):
    veterinarian = get_object_or_404(Veterinarian, pk=pk)
    return render(request, 'veterinarians/veterinarian_detail.html', {'veterinarian': veterinarian})
