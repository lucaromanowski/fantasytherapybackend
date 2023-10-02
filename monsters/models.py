from django.db import models

from patients.models import Patient
from therapists.models import Therapist


class Monster(models.Model):
    name = models.CharField(max_length=120)
    #therapist = models.ForeignKey(Therapist, related_name='monsters', on_delete=models.CASCADE) 
    patient = models.ForeignKey(Patient, related_name='monsters', on_delete=models.CASCADE)
    #image = models.ImageField()

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True) 

    def __str__(self):
        return f'{self.name}'