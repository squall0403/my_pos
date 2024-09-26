from django.urls import path
from . import views
from debug_toolbar.toolbar import debug_toolbar_urls

app_name = "suppliers"
urlpatterns = [
    path("", views.suppliers, name="suppliers"),
    path("detail/<slug:slug>", views.detail, name="detail"),
] + debug_toolbar_urls()
