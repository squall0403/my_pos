from django.utils import timezone
from django.db import models

# Create your models here.
class Sale(models.Model):
    pos = models.CharField(max_length=255, default="DXA", null=False)
    sale_date = models.DateTimeField(null=True, default=timezone.now)
    sale_item = models.ForeignKey(
        "inventories.Inventory", on_delete=models.RESTRICT, blank=True
    )
    quantity = models.IntegerField(blank=False, default=1)
    sub_total_price = models.IntegerField(blank=True, default=1)
    def __str__(self):
        return f"{self.pos}"
