# clients/views.py
from rest_framework import viewsets
from .models import Company, Facility
from .serializers import CompanySerializer, FacilitySerializer

class CompanyViewSet(viewsets.ModelViewSet):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer

class FacilityViewSet(viewsets.ModelViewSet):
    queryset = Facility.objects.all()
    serializer_class = FacilitySerializer