from rest_framework.generics import ListCreateAPIView,RetrieveUpdateDestroyAPIView 
from rest_framework.permissions import IsAuthenticated

from .serializer import CompanySerializer,RouteSerializer,ShipSerializer
from .models import Company,Route,Ship

class CompanyListView(ListCreateAPIView):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer
    permissions_classes = [IsAuthenticated]

class CompanyDetailView(RetrieveUpdateDestroyAPIView):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer 
    permission_classes = [IsAuthenticated]   

class RouteListCreateView(ListCreateAPIView):
    queryset = Route.objects.select_related('company')
    serializer_class = RouteSerializer
    permission_classes = [IsAuthenticated]

class RoutDetailView(RetrieveUpdateDestroyAPIView):
    queryset = Route.objects.select_related('company')
    serializer_class = RouteSerializer
    permission_classes =  [IsAuthenticated]    

class ShipListView(ListCreateAPIView):
    queryset = Ship.objects.select_related('company', 'route')
    serializer_class = ShipSerializer
    permission_classes = [IsAuthenticated]    

class ShipDetailView(RetrieveUpdateDestroyAPIView):
    queryset = Ship.objects.select_related('company', 'route')
    serializer_class = ShipSerializer   
    permission_classes = [IsAuthenticated]
    