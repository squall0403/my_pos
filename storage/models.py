from datetime import date, timedelta
from django.db import models


def expired_date(self):
    # Your calculation logic here
    return self.import_date + timedelta(days=self.item.expired_day)


# Create your models here.
class StorageItem(models.Model):
    item = models.ForeignKey(
        "inventories.Inventory", on_delete=models.RESTRICT, blank=True, default=44
    )
    quantity = models.IntegerField(default=0, blank=False)
    import_date = models.DateField(blank=False, default=date.today)
    expired_date = expired_date
    slug = models.SlugField(default="", null=True)

    def __str__(self):
        return f"{self.item}"
