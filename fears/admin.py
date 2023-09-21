from django.contrib import admin

from .models import Fear, FearIntensity


class FearIntensityInlineAdmin(admin.TabularInline):
	model = FearIntensity
	extra = 1

class FearAdmin(admin.ModelAdmin):
	list_display = ('title', 'created', 'updated')
	prepopulated_fields = {'slug': ('title',)}
	inlines = [FearIntensityInlineAdmin,]

admin.site.register(Fear, FearAdmin)