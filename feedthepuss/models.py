from typing import List
from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.


class User(AbstractUser):
    SEX_CHOICES = (("Male", "male"), ("Female", "female"))
    email = models.EmailField(null=False, blank=False, unique=True)
    age = models.PositiveSmallIntegerField(default=0)
    sex = models.CharField(choices=SEX_CHOICES, max_length=30, default="male")

    USERNAME_FIELD: str = "email"
    REQUIRED_FIELDS: List[str] = ["username"]

    def getPet(self):
        pet = self.pet
        return pet

    def __str__(self) -> str:
        return self.email


class Pet(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=30)
    weight = models.PositiveBigIntegerField(default=0)

    def addWeight(self, weight: int):
        self.weight += weight

    def Feed(self):
        self.addWeight(20)

    def __str__(self) -> str:
        return self.name
