from django.urls import path
from .views import DoctorProfileView, SiteSettingsView, FooterView

urlpatterns = [
    path("doctor/", DoctorProfileView.as_view(), name="doctor-profile"),
    path("settings/", SiteSettingsView.as_view(), name="site-settings"),
    path("footer/", FooterView.as_view(), name="footer"),
]
