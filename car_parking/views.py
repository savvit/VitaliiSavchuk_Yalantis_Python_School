from rest_framework import generics
from django_filters.rest_framework import DjangoFilterBackend

from car_parking.filter import DriverFilter
from car_parking.models import Driver, Vehicle
from car_parking.serializers import DriverListSerializer, VehicleListSerializer


class DriverListView(generics.ListCreateAPIView):
    """Returns drivers

    Works in three ways:
    first - returns all drivers completely if you pass to the url -> /drivers/driver/
    second - using DriverFilter returns filtered drivers by creation date
                                                            if you pass filtering parameters after /drivers/driver/?
    third - you can create objects with POST method
    """
    serializer_class = DriverListSerializer
    queryset = Driver.objects.all()
    # filter by date
    filter_backends = (DjangoFilterBackend,)
    filterset_class = DriverFilter


class DriverDetailView(generics.RetrieveUpdateDestroyAPIView):
    """ Returns a specific driver """
    serializer_class = DriverListSerializer
    queryset = Driver.objects.all()


class VehicleListView(generics.ListCreateAPIView):
    serializer_class = VehicleListSerializer

    def get_queryset(self):
        queryset = Vehicle.objects.all()
        with_drivers_param = self.request.query_params.get('with_drivers')
        print(with_drivers_param)

        if with_drivers_param == 'no':
            queryset = queryset.filter(driver_id__isnull=True)
        elif with_drivers_param == 'yes':
            queryset = queryset.filter(driver_id__isnull=False)

        return queryset


class VehicleDetailView(generics.RetrieveUpdateDestroyAPIView):
    """ Returns a specific vehicle """
    serializer_class = VehicleListSerializer
    queryset = Vehicle.objects.all()
