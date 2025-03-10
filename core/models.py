from django.db import models

# Create your models here.
class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now=True)

class NameModel(BaseModel):
    name = models.CharField(max_length=255)

    def __str__(self) -> str:
        return self.name
