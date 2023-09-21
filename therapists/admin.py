from django.contrib import admin

from .models import Therapist


class TherapistAdmin(admin.ModelAdmin):
	list_display = ['first_name', 'last_name', 'created', 'updated',]
	prepopulated_fields = {'slug' : ('first_name', 'last_name')}


admin.site.register(Therapist, TherapistAdmin)
