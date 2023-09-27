from django.contrib import admin

from .models import PatientTherapistRelationship

class PatientTherapistRelationshipAdmin(admin.ModelAdmin):
	list_display = ['therapist', 'patient', 'isPatientAccepting', 'created', 'updated',]

admin.site.register(PatientTherapistRelationship, PatientTherapistRelationshipAdmin)