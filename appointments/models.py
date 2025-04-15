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
