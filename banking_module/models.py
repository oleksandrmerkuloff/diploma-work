from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):
    email = models.EmailField(unique=True)


class Profile(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    date_of_birth = models.DateField(null=True, blank=True)
    country = models.CharField(max_length=50)
    phone_number = models.CharField(max_length=15)
    passport_number = models.CharField(max_length=15)

    def __str__(self):
        return self.user.username
