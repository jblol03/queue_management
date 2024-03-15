from django.db import models
from django.conf import settings

class Day(models.Model):
    DAYS_OF_WEEK = [
        ('MON', 'Monday'),
        ('TUE', 'Tuesday'),
        ('WED', 'Wednesday'),
        ('THU', 'Thursday'),
        ('FRI', 'Friday'),
        ('SAT', 'Saturday'),
        ('SUN', 'Sunday'),
    ]

    name = models.CharField(max_length=3, choices=DAYS_OF_WEEK)

    def __str__(self):
        return self.get_name_display()


class Appointment(models.Model):
    days = models.ManyToManyField(Day)
    slot = models.IntegerField()

    def __str__(self):
        return f'{", ".join(str(day) for day in self.days.all())} - {self.slot} slots'

class Booking(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    day = models.ForeignKey(Day, on_delete=models.CASCADE, default = 1)
    appointment = models.ForeignKey(Appointment, on_delete=models.CASCADE)
    user = models.ForeignKey('account.EndUser', on_delete=models.CASCADE, null = True)

    def __str__(self):
        return f'{self.appointment} - {self.user.name}'
    
