from rest_framework import viewsets, status
from rest_framework.response import Response
from .models import Day, Appointment, Booking
from .serializers import DaySerializer, AppointmentSerializer, BookingSerializer

class DayViewSet(viewsets.ModelViewSet):
    queryset = Day.objects.all()
    serializer_class = DaySerializer


class AppointmentViewSet(viewsets.ModelViewSet):
    queryset = Appointment.objects.all()
    serializer_class = AppointmentSerializer

    def perform_create(self, serializer):
        serializer.save()

class BookingViewSet(viewsets.ModelViewSet):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer

    def perform_create(self, serializer):
        appointment = serializer.validated_data['appointment']
        if appointment.slot <= 0:
            return Response({"error": "No slots available for this appointment"}, status=status.HTTP_400_BAD_REQUEST)
        appointment.slot -= 1
        appointment.save()
        serializer.save()

