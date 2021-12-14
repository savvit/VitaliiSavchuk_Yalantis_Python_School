from django.contrib import admin
from car_parking.models import Driver, Vehicle


class DriverAdmin(admin.ModelAdmin):
    list_display = ('id', 'first_name', 'last_name', 'created_at', 'updated_at')
    list_display_links = ('id', 'first_name', 'last_name')
    search_fields = ('first_name', 'last_name')


admin.site.register(Driver, DriverAdmin)


class VehicleAdmin(admin.ModelAdmin):
    list_display = ('id', 'driver_id', 'make', 'model', 'created_at', 'updated_at')
    list_display_links = ('id', 'driver_id', 'make', 'model')
    search_fields = ('make', 'model')


admin.site.register(Vehicle, VehicleAdmin)
