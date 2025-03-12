from django.db import models

# Create your models here.
class Menu(models.Model):
    title = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    inventory = models.IntegerField(null = True)

class Booking(models.Model):
    name = models.CharField(max_length=255)
    no_of_guest = models.IntegerField(null=True)
    booking_date = models.DateTimeField(null=True)

    def __str__(self):
        return f'{self.name}- {self.booking_date}'