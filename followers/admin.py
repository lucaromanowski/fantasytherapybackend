from django.contrib import admin

from .models import PatientTherapistConnection

class PatientTherapistConnectionAdmin(admin.ModelAdmin):
	list_display = ['therapist', 'patient', 'isPatientAccepting', 'created', 'updated',]

admin.site.register(PatientTherapistConnection, PatientTherapistConnectionAdmin)