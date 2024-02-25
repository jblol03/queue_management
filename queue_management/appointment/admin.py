from django.contrib import admin
from appointment.models import Appointment, Booking
# Register your models here.

admin.site.register([Appointment, Booking])