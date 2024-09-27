from csvexport.actions import csvexport
from django.contrib import admin
from .models import Inventory, UnitName,Category
# Register your models here.

class InventoryAdmin(admin.ModelAdmin):
  list_display = ("item_name", "unit_price","category","unit")
  prepopulated_fields = {"slug": ("item_name","item_name")}
  actions = [csvexport]

class UnitAdmin(admin.ModelAdmin):
  list_display = ("unit", "code")
  prepopulated_fields = {"slug": ("unit","code")}
  actions = [csvexport]

class CategoryAdmin(admin.ModelAdmin):
  list_display = ("name", "code")
  prepopulated_fields = {"slug": ("name","code")}
  actions = [csvexport]

admin.site.register(Inventory, InventoryAdmin)
admin.site.register(UnitName,UnitAdmin)
admin.site.register(Category,CategoryAdmin)