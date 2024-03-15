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

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        days = representation['days'].split(', ')
        return [{'day': day, 'slot': representation['slot']} for day in days]
    def get_booked_days(self, obj):
        bookings = Booking.objects.filter(appointment=obj)
        return [str(booking.day) for booking in bookings]


class BookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = '__all__'
