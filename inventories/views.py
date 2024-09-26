from django.template import loader
from django.http import HttpResponse
from django.shortcuts import render
from .models import Inventory
# Create your views here.

def inventories(request):
 inventories = Inventory .objects.all().values()
 template=loader.get_template('list.html')
 context = {
    'inventories': inventories,
  }
 return HttpResponse(template.render(context, request))

def detail(request, slug):
  inventory = Inventory.objects.get(slug=slug)
  template = loader.get_template('detail.html')
  context = {
    'inventory': inventory,
  }
  return HttpResponse(template.render(context, request))