from rest_framework import viewsets, status
from rest_framework.response import Response
from .models import Day, Appointment, Booking
from .serializers import DaySerializer, AppointmentSerializer, BookingSerializer
from django.contrib.auth.decorators import login_required


class DayViewSet(viewsets.ModelViewSet):
    queryset = Day.objects.all()
    serializer_class = DaySerializer

class AppointmentViewSet(viewsets.ModelViewSet):
    queryset = Appointment.objects.all()
    serializer_class = AppointmentSerializer

    def perform_create(self, serializer):
        serializer.save()

# @login_required
class BookingViewSet(viewsets.ModelViewSet):
    serializer_class = BookingSerializer
    queryset = Booking.objects.all()  

    def get_queryset(self):
        user = self.request.user
        if user.groups.filter(name='enduser').exists():
            return Booking.objects.filter(user=user)
        else:
            return Booking.objects.none()

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        day = serializer.validated_data['day']
        appointment = serializer.validated_data['appointment']

        if day.appointment_set.filter(id=appointment.id).exists():
            if appointment.slot <= 0:
                return Response({"error": "No slots available for this appointment"}, status=status.HTTP_400_BAD_REQUEST)
            else:
                appointment.slot -= 1
                appointment.save()
                self.perform_create(serializer)
                headers = self.get_success_headers(serializer.data)
                return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
        else:
            return Response({"error": "This appointment is not available for the chosen day"}, status=status.HTTP_400_BAD_REQUEST)