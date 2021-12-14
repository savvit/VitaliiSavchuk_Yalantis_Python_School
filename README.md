# REST API for car fleet with drivers
## Project made for Yalantis Python School
__Technologies that were used in the project:__
* [Python 3](https://www.python.org/)
* [Django 4.0](https://www.djangoproject.com/)
* [Django Rest Framwork](https://www.django-rest-framework.org/)
* [Django-filter](https://django-filter.readthedocs.io/en/latest/)
* [SQLite3](https://www.sqlite.org/index.html)
* [Postman - for API testing](https://www.postman.com/)

__This project have two models, using ForeignKey relationship:__
```
Driver:
 + id: int
 + first_name: str
 + last_name: str
 + created_at
 + updated_at
```
__and__
```
Vehicle
 + id: int
 + driver_id: FK to Driver
 + make: str
 + model: str
 + plate_number: str - format example "AA 1234 OO"
 + created_at
 + updated_at
```
__There are some open endpoints, like these:__
```
Driver:
GET /drivers/driver/
GET /drivers/driver/?created_at__gte=10-11-2021
GET /drivers/driver/?created_at__lte=16-11-2021
GET /drivers/driver/<driver_id>/
POST /drivers/driver/
UPDATE /drivers/driver/<driver_id>/
DELETE /drivers/driver/<driver_id>/

Vehicle:
GET /vehicles/vehicle/
GET /vehicles/vehicle/?with_drivers=yes
GET /vehicles/vehicle/?with_drivers=no
GET /vehicles/vehicle/<vehicle_id>
POST /vehicles/vehicle/
UPDATE /vehicles/vehicle/<vehicle_id>/
POST /vehicles/set_driver/<vehicle_id>/
DELETE /vehicles/vehicle/<vehicle_id>/
```
[__HOW TO DEPLOY THE PROJECT?__](https://github.com/savvit/VitaliiSavchuk_Yalantis_Python_School/blob/master/SETUP.md)
