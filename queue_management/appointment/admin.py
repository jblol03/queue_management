from django.contrib import admin
from appointment.models import Appointment, Booking, Day
# Register your models here.

admin.site.register([Appointment, Booking, Day])