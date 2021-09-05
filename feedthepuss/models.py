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

    USERNAME_FIELD: str = "email"
    REQUIRED_FIELDS: List[str] = ["username"]

    def save(self, *args, **kwargs):
        if not self.id:
            self.username = self.email
        super().save(*args, **kwargs)

    def __str__(self) -> str:
        return self.email

    def getPet(self):
        pet = self.pet
        return pet

    def cheat_days(self) -> int:
        return self.reports.filter(is_success=False).count()


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
    uuid = models.UUIDField(
        primary_key=True, auto_created=True, default=uuid4, editable=False
    )
    created_by = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="reports"
    )
    title = models.CharField(max_length=200)
    body = models.TextField()
    is_success = models.BooleanField(default=False)
    mealtime = models.DateTimeField()
    created_at = models.DateTimeField(
        auto_now_add=True,
    )

    def __str__(self) -> str:
        return self.title
