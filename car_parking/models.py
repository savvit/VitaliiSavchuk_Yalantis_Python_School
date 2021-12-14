from django.db import models


class Driver(models.Model):
    first_name = models.CharField(verbose_name='First name', max_length=100)
    last_name = models.CharField(verbose_name='Last name', max_length=100)
    created_at = models.DateField(verbose_name='Created at', auto_now_add=True)
    updated_at = models.DateField(verbose_name='Updated at', auto_now=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Vehicle(models.Model):
    driver_id = models.ForeignKey(Driver, on_delete=models.PROTECT, blank=True, null=True)
    make = models.CharField(verbose_name='Make', max_length=50)
    model = models.CharField(verbose_name='Model', max_length=50)
    plate_number = models.CharField(verbose_name='Plate number', max_length=20)
    created_at = models.DateField(verbose_name='Created at', auto_now_add=True)
    updated_at = models.DateField(verbose_name='Updated at', auto_now=True)

    def __str__(self):
        return self.model
