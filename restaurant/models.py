from django.db import models

# Create your models here.
class Menu (models.Model):
    ID = models.AutoField(primary_key=True)
    Name = models.CharField(max_length=255),
    No_of_guests = models.IntegerField(),
    BookingDate = models.DateField(),

    def __str__(self):
        return f'{self.title} : {str(self.price)}'

class Booking (models.Model):
    ID = models.AutoField(primary_key=True),
    Title = models.CharField(max_length=255),
    Price = models.DecimalField(),
    Inventory = models.IntegerField(),