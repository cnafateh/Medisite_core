from django.urls import path
from .views import DoctorProfileRetrieveUpdateAPIView

urlpatterns = [
    path("profile/", DoctorProfileRetrieveUpdateAPIView.as_view(), name="doctor-profile"),
]
