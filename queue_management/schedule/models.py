from django.db import models
from datetime import time

class Day(models.Model):
    name = models.CharField(max_length=20, unique=True)
    
    def __str__(self):
        return self.name

class Shift(models.Model):
    days = models.ManyToManyField(Day, related_name='shifts')
    name = models.CharField(max_length=20, unique=True)
    start_time = models.TimeField()
    end_time = models.TimeField()

    def __str__(self):
        return self.name
    
class Slot(models.Model):
    shift = models.ForeignKey(Shift, related_name='slots', on_delete=models.CASCADE)
    start_time = models.TimeField(default=time(0, 0))
    end_time = models.TimeField(default=time(0, 0))

    def __str__(self):
        days = ', '.join([str(day) for day in self.shift.days.all()])
        return f"{days} - {self.shift} - {self.start_time} to {self.end_time}"

class Schedule(models.Model):
    days = models.ManyToManyField(Day, related_name='schedules')
    shifts = models.ManyToManyField(Shift, related_name='schedules')

    def __str__(self):
        days = ', '.join([str(day) for day in self.days.all()])
        shifts = ', '.join([str(shift) for shift in self.shifts.all()])
        return f"Schedule: {days} - {shifts}"
    
class ScheduleManager(models.Manager):
    def create_schedule(self, days, shifts):
        schedule = self.create()
        for day in days:
            schedule.days.add(day)
        for shift in shifts:
            schedule.shifts.add(shift)
        return schedule
