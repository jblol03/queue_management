from rest_framework import serializers
from .models import Day, Shift, Slot, Schedule

class DaySerializer(serializers.ModelSerializer):
    class Meta:
        model = Day
        fields = ['id', 'name']

class ShiftSerializer(serializers.ModelSerializer):
    days = serializers.SlugRelatedField(
        many=True,
        queryset=Day.objects.all(),
        slug_field='name'
    )     
    class Meta:
        model = Shift
        fields = ['id', 'days', 'name', 'start_time', 'end_time',]

    def validate(self, data):
        name = data.get('name')
        days = data.get('days')
        
        if self.instance:
            if Shift.objects.filter(name=name, days__in=days).exclude(id=self.instance.id).exists():
                raise serializers.ValidationError("A shift with this name already exists on the selected days.")
        else:
            if Shift.objects.filter(name=name, days__in=days).exists():
                raise serializers.ValidationError("A shift with this name already exists on the selected days.")
        
        return data

class SlotSerializer(serializers.ModelSerializer):
    shift = ShiftSerializer()

    class Meta:
        model = Slot
        fields = ['id', 'start_time', 'end_time', 'shift']

    def validate(self, data):
        shift = data['shift']
        if not (shift['start_time'] <= data['start_time'] <= data['end_time'] <= shift['end_time']):
            raise serializers.ValidationError("Slot's start time and end_time should be within the shift's start time and end time")
        return data

class ScheduleSerializer(serializers.ModelSerializer):
    days = DaySerializer(many=True)
    shifts = ShiftSerializer(many=True)

    class Meta:
        model = Schedule
        fields = '__all__'

    def create(self, validated_data):
        days_data = validated_data.pop('days')
        shifts_data = validated_data.pop('shifts')
        schedule = Schedule.objects.create(**validated_data)
        for day_data in days_data:
            Day.objects.create(schedule=schedule, **day_data)
        for shift_data in shifts_data:
            shift = ShiftSerializer.create(ShiftSerializer(), validated_data=shift_data)
            schedule.shifts.add(shift)
        return schedule