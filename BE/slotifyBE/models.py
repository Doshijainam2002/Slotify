from django.db import models
from django.contrib.auth.models import User

class OwnerProfile(models.Model):
    firstName = models.CharField(max_length=50, null=False)
    lastName = models.CharField(max_length=50, null=False)
    emailId = models.EmailField(max_length=255, unique=True, null=False)
    password = models.CharField(max_length=255, null=False)
    contactNumber = models.CharField(max_length=10, unique=True, null=False)
    idProof = models.URLField(max_length=500, blank=True, null=True)
    verified = models.BooleanField(default=False)

class ParkingLot(models.Model):
    name = models.CharField(max_length=255)
    location = models.CharField(max_length=255)
    total_spaces = models.PositiveIntegerField()
    available_spaces = models.PositiveIntegerField()
    registered_by = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
