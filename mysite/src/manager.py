from datetime import date, timedelta
from django.db import models
from django.core.validators import MaxValueValidator

class Booking(models.Model):
    email = models.EmailField(max_length=100)
    number = models.CharField(max_length=50)
    time = models.DateField()
    slot = models.PositiveIntegerField(validators=[MaxValueValidator(99999)])
    registered_time = models.DateField()

    def expiringReservation(self):
        if self.time + timedelta(365) < date.today():
            self.delete();
            return True
        return False

    def __hash__(self) -> int:
        return hash((self.email, self.number, self.time, self.slot, self.registered_time))

    def __eq__(self, obj) -> bool:
        if not isinstance(obj, Booking):
            return False
        return (
            self.email == obj.email and
            self.number == obj.number and
            self.slot == obj.slot and
            self.time == obj.time and
            self.registered_time == obj.registered_time
        )