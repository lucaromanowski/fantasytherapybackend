from django.contrib import admin

from .models import Patient


class PatientAdmin(admin.ModelAdmin):
	list_display = ['nickname', 'created', 'updated']

admin.site.register(Patient, PatientAdmin)