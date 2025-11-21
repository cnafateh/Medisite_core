from django.contrib import admin
from .models import SiteSettings, DoctorProfile

@admin.register(SiteSettings)
class SiteSettingsAdmin(admin.ModelAdmin):
    list_display = ('clinic_address', 'clinic_phone', 'email', 'updated_at')


admin.site.register(DoctorProfile)