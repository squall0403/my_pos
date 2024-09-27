from django.urls import path
from . import views
from debug_toolbar.toolbar import debug_toolbar_urls

urlpatterns = [
    path('', views.main, name='main'),
    path('sale_form/', views.sale_form, name='sale_form'),
] + debug_toolbar_urls()
