from django.db import models
from django.contrib.auth.models import AbstractUser

class Appointment(models.Model):
    pet_name = models.CharField(max_length=100)
    owner_name = models.CharField(max_length=100)
    date = models.DateField()
    time = models.TimeField()
    description = models.TextField()

    def __str__(self):
        return f"{self.pet_name} - {self.date} {self.time}"


class Vet(models.Model):
    name = models.CharField(max_length=100)
    specialty = models.CharField(max_length=100)
    contact_number = models.CharField(max_length=15)
    image = models.ImageField(upload_to='images/', blank=True, null=True)  # Fixed upload path

    def __str__(self):
        return self.name


class Service(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.FloatField()
    image = models.ImageField(upload_to='images/', blank=True, null=True)  # Fixed upload path

    def __str__(self):
        return self.name


class Feedback(models.Model):
    RATING_CHOICES = [
        (1, 'Very Poor'),
        (2, 'Poor'),
        (3, 'Average'),
        (4, 'Good'),
        (5, 'Excellent'),
    ]

    name = models.CharField(max_length=100, help_text="Enter your full name")
    contact_details = models.CharField(max_length=100, help_text="Enter your contact", blank=True, null=True)  # Fixed field name
    rating = models.IntegerField(choices=RATING_CHOICES, help_text="Rate our service (1 to 5)")
    description = models.TextField(help_text="Leave a comment about your experience", blank=True, null=True)

    def __str__(self):
        return f"Feedback from {self.name} ({self.rating}/5)"


class User(AbstractUser):
    phone_number = models.CharField(max_length=15, blank=True, null=True)
    profile_picture = models.ImageField(upload_to='profile_pics/', blank=True, null=True)

    def __str__(self):
        return self.username
