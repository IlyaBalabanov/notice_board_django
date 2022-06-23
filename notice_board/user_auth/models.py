from django.db import models
from django.contrib.auth.models import AbstractUser


class Account(AbstractUser):
    image = models.ImageField(upload_to='images/', null=True, blank=True)
    address = models.ForeignKey('Address', on_delete=models.CASCADE, null=True)

    def __str__(self):
        return f'[{self.username}] {self.address.__str__()}'


class Address(models.Model):
    city = models.CharField(max_length=64)
    population_centers = models.CharField(max_length=64, null=True, blank=True)
    street = models.CharField(max_length=64)
    house = models.CharField(max_length=64)
    building = models.CharField(max_length=64, null=True, blank=True)
    flat = models.CharField(max_length=64)

    def short(self):
        return f'{self.street}, {self.house}к{self.building}'

    def __str__(self):
        return f'{self.city}, ул. {self.street}, д. {self.house} к{self.building}, кв {self.flat}'
