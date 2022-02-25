from django.contrib import admin
from .models import *
class ScheduleInLine(admin.TabularInline):
	model=Schedule
	extra=5
class DoctorAdmin(admin.ModelAdmin):
	inlines=[ScheduleInLine]
admin.site.register(Doctor,DoctorAdmin)

admin.site.register(Patient)
admin.site.register(Review)
admin.site.register(Department)