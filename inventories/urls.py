from django.urls import path
from . import views
from debug_toolbar.toolbar import debug_toolbar_urls

app_name = "inventories"
urlpatterns = [
    path("", views.inventories, name="inventories"),
    path("inventories/detail/<slug:slug>", views.detail, name="detail"),
] + debug_toolbar_urls()
