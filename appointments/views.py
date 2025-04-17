from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.template.loader import render_to_string
from weasyprint import HTML
from django.http import HttpResponse
from .models import Appointment
from .models import MedicalRecord
from .forms import AppointmentForm
from .forms import MedicalRecordForm
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

@login_required
def create_medical_record(request, appointment_id):
    appointment = get_object_or_404(Appointment, id=appointment_id)

    if hasattr(appointment, 'medical_record'):
        return redirect('appointments:view_medical_record', appointment_id=appointment.id)

    if request.method == 'POST':
        form = MedicalRecordForm(request.POST)
        if form.is_valid():
            record = form.save(commit=False)
            record.appointment = appointment
            record.save()
            return redirect('appointments:view_medical_record', appointment_id=appointment.id)
    else:
        form = MedicalRecordForm()

    return render(request, 'appointments/medical_record_form.html', {'form': form, 'appointment': appointment})

@login_required
def view_medical_record(request, appointment_id):
    appointment = get_object_or_404(Appointment, id=appointment_id)
    record = get_object_or_404(MedicalRecord, appointment=appointment)
    return render(request, 'appointments/medical_record_detail.html', {'record': record, 'appointment': appointment})

@login_required
def edit_medical_record(request, appointment_id):
    appointment = get_object_or_404(Appointment, id=appointment_id)
    medical_record = get_object_or_404(MedicalRecord, appointment=appointment)
    
    if request.method == 'POST':
        form = MedicalRecordForm(request.POST, instance=medical_record)
        if form.is_valid():
            form.save()
            return redirect('appointments:view_medical_record', appointment_id=appointment.id)
    else:
        form = MedicalRecordForm(instance=medical_record)
    
    return render(request, 'appointments/medical_record_edit.html', {'form': form, 'appointment': appointment})

@login_required
def delete_medical_record(request, appointment_id):
    appointment = get_object_or_404(Appointment, id=appointment_id)
    medical_record = get_object_or_404(MedicalRecord, appointment=appointment)

    if request.method == 'POST':
        medical_record.delete()
        messages.success(request, f'Medical record for {appointment.pet.name} was successfully deleted.')
        return redirect('appointments:view_medical_record', appointment_id=appointment.id)
    
    return render(request, 'appointments/medical_record_confirm_delete.html', {'medical_record': medical_record})

@login_required
def view_prescription(request, record_id):
    record = get_object_or_404(MedicalRecord, pk=record_id)
    appointment = record.appointment  # Obtém o appointment relacionado ao medical record
    return render(request, 'appointments/prescription.html', {'record': record, 'appointment': appointment})

@login_required
def generate_prescription_pdf(request, record_id):
    record = get_object_or_404(MedicalRecord, pk=record_id)
    appointment = record.appointment  # Obtém o appointment relacionado ao medical record
    html = render(request, 'appointments/prescription.html', {'record': record, 'appointment': appointment}).content.decode('utf-8')
    pdf_file = HTML(string=html).write_pdf()
    
    response = HttpResponse(pdf_file, content_type='application/pdf')
    response['Content-Disposition'] = f'filename=prescription_{record_id}.pdf'
    return response
