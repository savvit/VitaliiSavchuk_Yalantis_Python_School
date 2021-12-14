from django.contrib import admin
from django.urls import path
from car_parking.views import (DriverListView,
                               DriverDetailView,
                               VehicleListView,
                               VehicleDetailView,)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('drivers/driver/', DriverListView.as_view()),
    path('drivers/driver/<int:pk>/', DriverDetailView.as_view()),
    path('vehicles/vehicle/', VehicleListView.as_view()),
    path('vehicles/vehicle/<int:pk>/', VehicleDetailView.as_view()),
]
