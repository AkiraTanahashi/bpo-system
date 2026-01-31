# clients/serializers.py
from rest_framework import serializers
from .models import Company, Facility

class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = '__all__' # 全部の項目をJSONにする

class FacilitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Facility
        fields = '__all__'