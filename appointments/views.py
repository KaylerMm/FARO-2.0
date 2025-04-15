from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Appointment
from .forms import AppointmentForm
from django.utils import timezone

@login_required
def appointment_list(request):
    appointments = Appointment.objects.all()
    today = timezone.now().date()

    appointments_today = Appointment.objects.filter(date__date=today)

    return render(request, 'appointments/appointment_list.html', {
        'appointments': appointments,
        'appointments_today': appointments_today,
        'today': today,
    })

@login_required
def appointment_create(request):
    if request.method == 'POST':
        form = AppointmentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('appointments:appointment_list')
    else:
        form = AppointmentForm()
    return render(request, 'appointments/appointment_form.html', {'form': form})

@login_required
def appointment_list(request):
    appointments = Appointment.objects.select_related('pet', 'veterinarian').all()
    return render(request, 'appointments/appointment_list.html', {'appointments': appointments})

@login_required
def appointment_detail(request, pk):
    appointment = get_object_or_404(Appointment, pk=pk)
    return render(request, 'appointments/appointment_detail.html', {'appointment': appointment})

@login_required
def appointment_update(request, pk):
    appointment = get_object_or_404(Appointment, pk=pk)
    if request.method == 'POST':
        form = AppointmentForm(request.POST, instance=appointment)
        if form.is_valid():
            form.save()
            return redirect('appointments:appointment_list')
    else:
        form = AppointmentForm(instance=appointment)
    return render(request, 'appointments/appointment_form.html', {'form': form})

@login_required
def appointment_delete(request, pk):
    appointment = get_object_or_404(Appointment, pk=pk)
    if request.method == 'POST':
        appointment.delete()
        return redirect('appointments:appointment_list')
    return render(request, 'appointments/appointment_confirm_delete.html', {'appointment': appointment})
