from django.db import models

# Create your models here.
class Supplier(models.Model):
    code = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    contact_name = models.CharField(max_length=255, default="")
    email = models.EmailField(max_length=255, null=False, default="")
    address = models.CharField(max_length=255, null=False, default="")
    district = models.CharField(max_length=255, null=False, default="")
    city = models.CharField(max_length=255, null=False, default="")
    country_code = models.CharField(max_length=255, null=False, default="")
    phone = models.CharField(max_length=255)
    slug = models.SlugField(default="", null=False)

    def __iter__(self):
        for field_name in ['code', 'name','contact_name','email','phone','address','district','city','country_code']:
            yield field_name, getattr(self, field_name)
    def __str__(self):
        return f"{self.name}"
