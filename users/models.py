from django.contrib.auth.models import AbstractUser
from django.core.validators import RegexValidator
from django.db import models


class User(AbstractUser):
    phone_number = models.CharField(
        null=True,
        validators=[RegexValidator(r"^((8|\+7)[\- ]?)?(\(?\d{3}\)?[\- ]?)?[\d\- ]{7,10}$")],
        max_length=15,
    )
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    third_name = models.CharField(max_length=50)

    class Meta:
        indexes = [
            models.Index(fields=['last_name', 'first_name', 'third_name']),
        ]
