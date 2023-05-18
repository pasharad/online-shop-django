from django.db import models
from django.contrib.auth.models import AbstractUser
from core.models import BaseModel
# Create your models here.

class Address(BaseModel):
    addresses = models.CharField(max_length=255, blank=True, null=True)
    phone = models.CharField(max_length=255, blank=True, null=True)
    postal_code = models.CharField(max_length=255, blank=True, null=True)


class User(AbstractUser):
    address = models.ManyToManyField(Address, related_name='user_address')

