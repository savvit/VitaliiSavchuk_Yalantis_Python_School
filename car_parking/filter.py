from django_filters import rest_framework as filters
from car_parking.models import Driver


class DriverFilter(filters.FilterSet):
    created_at__gte = filters.DateFilter(field_name="created_at", lookup_expr='gte')
    created_at__lte = filters.DateFilter(field_name="created_at", lookup_expr='lte')

    class Meta:
        model = Driver
        fields = '__all__'
