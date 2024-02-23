from rest_framework import serializers
from .models import Day, Appointment, Booking

class DaySerializer(serializers.ModelSerializer):
    class Meta:
        model = Day
        fields = '__all__'
        
class AppointmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Appointment
        fields = ['days', 'slot']



class BookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = '__all__'
