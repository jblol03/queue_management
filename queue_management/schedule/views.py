from rest_framework import generics
from .models import Day, Shift, Slot
from . serializers import DaySerializer, ShiftSerializer, SlotSerializer

class DayListCreateView(generics.ListCreateAPIView):
    queryset = Day.objects.all()
    serializer_class = DaySerializer

class ShiftListCreateView(generics.ListCreateAPIView):
    queryset = Shift.objects.all()
    serializer_class  = ShiftSerializer

class SlotListCreateView(generics.ListCreateAPIView):
    queryset = Slot.objects.all()
    serializer_class = SlotSerializer