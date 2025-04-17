from django.db import models
from veterinarians.models import Veterinarian
from pets.models import Pet

class Appointment(models.Model):
    pet = models.ForeignKey(Pet, on_delete=models.CASCADE, related_name='appointments')
    veterinarian = models.ForeignKey(Veterinarian, on_delete=models.CASCADE, related_name='appointments')
    date = models.DateTimeField()
    reason = models.TextField()

    def __str__(self):
        return f"{self.pet.name}'s appointment with {self.veterinarian.name} in {self.date}"

    class Meta:
        ordering = ['date']

class MedicalRecord(models.Model):
    appointment = models.OneToOneField(Appointment, on_delete=models.CASCADE, related_name='medical_record')
    description = models.TextField(verbose_name='Appointment Description')
    medications = models.TextField(blank=True, verbose_name='Medicine Prescribed')
    instructions = models.TextField() 
    notes = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.appointment.pet.name}'s recrod on {self.appointment.date.strftime('%d/%m/%Y')}"

