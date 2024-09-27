from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader
from .form import SaleForm
from .models import Sale

# Create your views here.
def main(request):
  template = loader.get_template('main.html')
  return HttpResponse(template.render())

def sale_form(request):
  sales = Sale.objects.all()
  template=loader.get_template('sale_form.html')
  context = {
    'sales': sales,
    'form' : SaleForm
  }
  if request.method == "POST":
        form = SaleForm(request.POST)
        if form.is_valid():
            sale = form.save(commit=False)
            sale.sub_total_price = sale.sale_item.unit_price * sale.quantity
            print(sale.sub_total_price)
            sale.save()
  return HttpResponse(template.render(context, request))