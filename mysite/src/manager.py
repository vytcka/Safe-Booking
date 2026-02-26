from datetime import date, timedelta
from django.db import models
from django.core.validators import MaxValueValidator
from django.core.exceptions import ValidationError

class Booking(models.Model):
    """The Booking class incoreperates Object-relational Mapping to create a map bookings on the backend and render
    them in the frontend once changed."""
    email = models.EmailField(max_length=100)
    number = models.CharField(max_length=50)
    time = models.DateField()
    slot = models.PositiveIntegerField(validators=[MaxValueValidator(99999)])
    registered_time = models.DateField()
    isValid = models.BooleanField(default=True)

    def expiringReservation(self)-> bool:
        """Remove a expiring booking... can be changed but currently a year in advance."""
        if self.time + timedelta(365) < date.today():
            self.delete();
            return True
        return False
    
    def oneReservationPerUser(self)-> bool:
        """Making sure that a user can only make a single booking per user."""
        bookings = Booking.objects.filter(email=self.email)
        if bookings.count() < 2:
            self.isValid = True
            
            return True
        else:
            self.isValid = False
            raise ValidationError("User already has 2 bookings.")
        
        

    def __hash__(self) -> int:
        """Hashing object"""
        return hash((self.email, self.number, self.time, self.slot, self.registered_time))

    def __eq__(self, obj) -> bool:
        """checking if the objects are the same."""
        if not isinstance(obj, Booking):
            return False
        return (
            self.email == obj.email and
            self.number == obj.number and
            self.slot == obj.slot and
            self.time == obj.time and
            self.registered_time == obj.registered_time
        )