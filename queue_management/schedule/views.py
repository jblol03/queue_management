from rest_framework import generics, status, viewsets
from rest_framework.response import Response
from .models import Day, Shift, Slot, Schedule
from . serializers import DaySerializer, ShiftSerializer, SlotSerializer, ScheduleSerializer

class DayListCreateView(generics.GenericAPIView):
    queryset = Day.objects.all()
    serializer_class = DaySerializer

    def get(self, request):
        days = self.get_queryset()
        serializer = DaySerializer(days, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = DaySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        day = self.get_object()
        day.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    def put(self, request, pk):
        day = self.get_object()
        serializer = DaySerializer(day, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, pk):
        day = self.get_object()
        serializer = DaySerializer(day, data=request.data, partial=True) # set partial=True to update a data partially
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ShiftListCreateView(generics.GenericAPIView):
    queryset = Shift.objects.all()
    serializer_class = ShiftSerializer

    def get(self, request):
        shifts = self.get_queryset()
        serializer = ShiftSerializer(shifts, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = ShiftSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        shift = self.get_object()
        shift.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    def put(self, request, pk):
        shift = self.get_object()
        serializer = ShiftSerializer(shift, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, pk):
        shift = self.get_object()
        serializer = ShiftSerializer(shift, data=request.data, partial=True) # set partial=True to update a data partially
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class SlotListCreateView(generics.GenericAPIView):
    queryset = Slot.objects.all()
    serializer_class = SlotSerializer

    def get(self, request):
        slots = self.get_queryset()
        serializer = SlotSerializer(slots, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = SlotSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        slot = self.get_object()
        slot.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    def put(self, request, pk):
        slot = self.get_object()
        serializer = SlotSerializer(slot, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, pk):
        slot = self.get_object()
        serializer = SlotSerializer(slot, data=request.data, partial=True) # set partial=True to update a data partially
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ScheduleViewSet(viewsets.ModelViewSet):
    queryset = Schedule.objects.all()
    serializer_class = ScheduleSerializer

    def list(self, request):
        queryset = Schedule.objects.all()
        serializer = ScheduleSerializer(queryset, many=True)
        return Response(serializer.data)

    def create(self, request):
        serializer = ScheduleSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)