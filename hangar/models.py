from django.contrib.auth.models import User
from django.db import models


class Feature(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return str(self.name)


class Astronaut(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)

    @property
    def full_name(self):
        return f"{self.first_name} {self.last_name}"

    def __str__(self):
        return self.full_name


class Hangar(models.Model):
    name = models.CharField(max_length=100)
    rackets_number = models.IntegerField()

    def __str__(self):
        return str(self.name)


class Racket(models.Model):
    name = models.CharField(max_length=255)
    type = models.CharField(max_length=63)
    height = models.IntegerField()
    features = models.ManyToManyField(Feature, related_name="rackets")
    astronauts = models.ManyToManyField(Astronaut, related_name="rackets")


class RacketFlight(models.Model):
    flight_time = models.DateTimeField(auto_now_add=True)
    racket = models.ForeignKey(Racket, on_delete=models.CASCADE, related_name="flights")
    hangar = models.ForeignKey(Hangar, on_delete=models.CASCADE, related_name="flights")

    class Meta:
        ordering = ("flight_time", )

    def __str__(self):
        return self.racket.name + str(self.flight_time)


class Order(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)


class Ticket(models.Model):
    racket_flight = models.ForeignKey(RacketFlight, on_delete=models.CASCADE, related_name="tickets")
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name="tickets")
    racket_number = models.IntegerField()

    class Meta:
        unique_together = ("racket_flight", "racket_number")
