from typing import List
from django.db import models
from django.contrib.auth.models import AbstractUser
from uuid import uuid4
# Create your models here.


class User(AbstractUser):
    SEX_CHOICES = (("Male", "male"), ("Female", "female"))
    email = models.EmailField(null=False, blank=False, unique=True)
    age = models.PositiveSmallIntegerField(default=0)
    sex = models.CharField(choices=SEX_CHOICES, max_length=30, default="male")
    #: added a cheat days field so that we know whether to starve the cat or not
    cheat_days = models.PositiveSmallIntegerField(default=0)
    USERNAME_FIELD: str = "email"
    REQUIRED_FIELDS: List[str] = ["username"]

    def resetCheatDay(self):
        self.cheat_days = 0

    def incCheatDay(self):
        self.cheat_days += 1

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


class Report(models.Model):
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    # TODO: if using boolean field to distinguish meals and cheat is a bad idea, then feel free to seperate to a new table
    is_success = models.BooleanField(default=False)
    uuid = models.UUIDField(primary_key=True, auto_created=True, default=uuid4, editable=False)
    created_at = models.DateTimeField(auto_created=True)
    mealtime = models.DateTimeField()
    title = models.CharField(max_length=200)
    body = models.TextField()

    def __str__(self) -> str:
        return self.title

