from django.db import models


def doctor_profile_upload_path(instance, filename):
    return f"doctor/profile/{filename}"


class DoctorProfile(models.Model):
    full_name = models.CharField(max_length=150)
    title = models.CharField(max_length=150)
    biography = models.TextField()
    medical_registry_number = models.CharField(max_length=100)
    experience_years = models.PositiveSmallIntegerField()
    clinic_address = models.TextField()
    clinic_phone = models.CharField(max_length=50)
    hospital_name = models.CharField(max_length=150)
    profile_image = models.ImageField(upload_to=doctor_profile_upload_path)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.full_name
