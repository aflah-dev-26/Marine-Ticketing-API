from rest_framework import serializers
from .models import Company,Route,Ship

class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = ['name','registration_number']

class RouteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Route
        fields = ['name','departure_port','arrival_port','departure_time','arrival_time','distance_km']

class ShipSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ship
        fields = ['route','name','image','capacity','price']    
        