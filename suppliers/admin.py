from django.contrib import admin
from .models import Supplier

# Register your models here.
class SupplierAdmin(admin.ModelAdmin):
  list_display = ("name", "code", "phone")
  prepopulated_fields = {"slug": ("name","code")}

admin.site.register(Supplier, SupplierAdmin)