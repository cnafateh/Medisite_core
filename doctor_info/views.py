from rest_framework import generics
from .models import DoctorProfile
from .serializers import DoctorProfileSerializer

class DoctorProfileRetrieveUpdateAPIView(generics.RetrieveUpdateAPIView):
    queryset = DoctorProfile.objects.all()
    serializer_class = DoctorProfileSerializer

    def get_object(self):
        return DoctorProfile.objects.first()
