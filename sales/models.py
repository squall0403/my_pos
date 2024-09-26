from datetime import date
from django.utils import timezone
from django.db import models

# Create your models here.
class Sale(models.Model):
    pos = models.CharField(max_length=255, default="", null=False)
    sale_date = models.DateTimeField(null=True, default=timezone.now)
    sale_item = models.CharField(max_length=255, default="", null=False)

    def __str__(self):
        return f"{self.pos}"
