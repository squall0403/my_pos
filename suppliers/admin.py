from django.contrib import admin
from .models import Supplier
from csvexport.actions import csvexport

# Register your models here.
class SupplierAdmin(admin.ModelAdmin):
  list_display = ("name", "code", "phone")
  prepopulated_fields = {"slug": ("name","code")}
  actions = [csvexport]

admin.site.register(Supplier, SupplierAdmin)