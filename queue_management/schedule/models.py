from django.db import models

# Create your models here.

class Day(models.Model):
    name = models.CharField(max_length=20, unique=True)
    
    def __str__(self):
        return self.name

class Shift(models.Model):
    name = models.CharField(max_length=20, unique=True)
    start_time = models.TimeField()
    end_time = models.TimeField()

    def __str__(self):
        return self.name
    
class Slot(models.Model):
    day = models.ForeignKey(Day, on_delete=models.CASCADE)
    shift = models.ForeignKey(Shift, on_delete=models.CASCADE)
    start_time = models.TimeField()
    end_time = models.TimeField()

    def __str__(self):
        return f"{self.day} - {self.shift} - {self.start_time} to {self.end_time}"