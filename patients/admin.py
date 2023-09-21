from django.contrib import admin

from .models import Patient


class PatientAdmin(admin.ModelAdmin):
	list_display = ['nickname', 'created', 'updated']
	prepopulated_fields = {'slug': ('nickname',)}

admin.site.register(Patient, PatientAdmin)