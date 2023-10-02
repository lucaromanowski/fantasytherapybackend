from django.contrib import admin

from .models import Monster

class MonsterAdmin(admin.ModelAdmin):
    list_display = ['name', 'patient', 'created', 'updated',]
admin.site.register(Monster, MonsterAdmin)
