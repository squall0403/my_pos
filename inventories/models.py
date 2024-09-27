from django.db import models

class Inventory(models.Model):
    sku = models.CharField(max_length=255)
    item_name = models.CharField(max_length=255)
    category = models.ForeignKey(
        "Category", on_delete=models.SET_NULL, blank=True, null=True
    )
    supplier = models.ForeignKey(
        "suppliers.Supplier", on_delete=models.PROTECT, blank=True
    )
    unit = models.ForeignKey("UnitName", null=True, on_delete=models.SET_NULL)
    unit_price = models.IntegerField(null=False, default=0)
    expired_day = models.IntegerField(blank=True, default=1)
    slug = models.SlugField(default="", null=False)

    class Meta:
        verbose_name_plural = "inventories"
    def __iter__(self):
            for field_name in ['sku', 'item_name','category','supplier','unit','unit_price']:
                yield field_name, getattr(self, field_name)
    def __str__(self):
        return f"{self.item_name}"


class UnitName(models.Model):
    unit = models.CharField(max_length=255, null=False, default="")
    code = models.CharField(max_length=4, null=False, default="")
    slug = models.SlugField(default="", null=False)

    class Meta:
        verbose_name_plural = "Units"

    def __str__(self):
        return f"{self.unit}"


class Category(models.Model):
    name = models.CharField(max_length=255, null=False, default="")
    code = models.CharField(max_length=3, null=False, default="")
    slug = models.SlugField(default="", null=False)

    class Meta:
        verbose_name_plural = "categories"

    def __str__(self):
        return f"{self.name}"
