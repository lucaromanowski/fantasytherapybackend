from django.contrib import admin

from .models import Therapist


class TherapistAdmin(admin.ModelAdmin):
	list_display = ['first_name', 'last_name', 'created', 'updated',]

admin.site.register(Therapist, TherapistAdmin)
