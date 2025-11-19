from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/core/", include("core.urls")),
    path("api/doctor/", include("doctor_info.urls")),
    path("api/blog/", include("blog.urls")),
]
