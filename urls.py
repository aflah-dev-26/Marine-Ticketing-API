from django.urls import path
from .views import CompanyListView,CompanyDetailView,RouteListCreateView,RoutDetailView,ShipListView,ShipDetailView

urlpatterns = [
    path('companies/',CompanyListView.as_view(),name='company-list'),
    path('companies/<int:pk>/',CompanyDetailView.as_view(),name='company-detail'),

    path('routes/',RouteListCreateView.as_view(),name='route-list'),
    path('routes/<int:pk>/',RoutDetailView.as_view(),name='route-detail'),

    path('ships/',ShipListView.as_view(),name='ship-list'),
    path('ships/<int:pk>/',ShipDetailView.as_view(),name='ship-detail'),
]