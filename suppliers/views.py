from django.template import loader
from django.http import HttpResponse
from django.shortcuts import render
from .models import Supplier
# Create your views here.

def suppliers(request):
 suppliers = Supplier.objects.all()
 template=loader.get_template('supplier_list.html')
 context = {
    'suppliers': suppliers,
  }
 return HttpResponse(template.render(context, request))

def detail(request, slug):
  supplier = Supplier.objects.get(slug=slug)
  suppliers = Supplier.objects.all()
  template = loader.get_template('supplier_detail.html')
  context = {
    'suppliers':suppliers,
    'supplier': supplier,
  }
  return HttpResponse(template.render(context, request))