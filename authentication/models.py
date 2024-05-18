from django.contrib.auth.models import AbstractUser
from django.db import models


class MyUser(AbstractUser):
    balance = models.IntegerField(default=0)
    is_verified = models.BooleanField(default=False)

    def __str__(self):
        return self.username
