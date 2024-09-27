from django.contrib import admin
from django.urls import include, path
from debug_toolbar.toolbar import debug_toolbar_urls

urlpatterns = [
    path("inventories/", include("inventories.urls")),
    path('sales/', include("sales.urls")),
    path('suppliers/', include("suppliers.urls")),
    path("admin/", admin.site.urls),
] + debug_toolbar_urls()
