from django.contrib import admin
from .models import StorageItem
from csvexport.actions import csvexport

# Register your models here.
class StorageItemAdmin(admin.ModelAdmin):
    list_display = ("item", "quantity","expired_date")
    prepopulated_fields = {"slug": ("item", "quantity","import_date")}  
    actions = [csvexport]

admin.site.register(StorageItem, StorageItemAdmin)
