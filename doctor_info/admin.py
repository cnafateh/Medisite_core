from django.contrib import admin
from .models import DoctorProfile

@admin.register(DoctorProfile)
class DoctorProfileAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'title', 'medical_registry_number', 'experience_years', 'clinic_phone', 'hospital_name')
