from django.db import models
from django.contrib.auth.models import AbstractUser
from core.models import BaseModel
from django.utils.text import slugify
# Create your models here.

class User(AbstractUser):
    phone = models.CharField(max_length=255, blank=True, null=True)
    slug = models.SlugField(unique=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.username)
        super().save(*args, **kwargs)


class Address(BaseModel):
    addresses = models.CharField(max_length=255, blank=True, null=True)
    postal_code = models.CharField(max_length=255, blank=True, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.slug
