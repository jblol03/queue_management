from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Day, Shift, Slot
from .serializers import DaySerializer, ShiftSerializer, SlotSerializer

class CombinedScheduleView(APIView):
    def get(self, request):
        days = Day.objects.all()
        shifts = Shift.objects.all()
        slots = Slot.objects.all()

        day_serializer = DaySerializer(days, many=True)
        shift_serializer = ShiftSerializer(shifts, many=True)
        slot_serializer = SlotSerializer(slots, many=True)

        combined_data = {
            'days': day_serializer.data,
            'shifts': shift_serializer.data,
            'slots': slot_serializer.data,
        }

        return Response(combined_data, status=status.HTTP_200_OK)
