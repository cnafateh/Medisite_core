from django.urls import path
from .views import SiteSettingsRetrieveUpdateAPIView

urlpatterns = [
    path("settings/", SiteSettingsRetrieveUpdateAPIView.as_view(), name="site-settings"),
]
