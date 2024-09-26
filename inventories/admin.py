from django.contrib import admin
from .models import Inventory, UnitName,Category
# Register your models here.
class InventoryAdmin(admin.ModelAdmin):
  list_display = ("item_name", "unit_price","category","supplier")
  prepopulated_fields = {"slug": ("item_name","item_name")}

class UnitAdmin(admin.ModelAdmin):
  list_display = ("unit", "code")
  prepopulated_fields = {"slug": ("unit","code")}

class CategoryAdmin(admin.ModelAdmin):
  list_display = ("name", "code")
  prepopulated_fields = {"slug": ("name","code")}

admin.site.register(Inventory, InventoryAdmin)
admin.site.register(UnitName,UnitAdmin)
admin.site.register(Category,CategoryAdmin)