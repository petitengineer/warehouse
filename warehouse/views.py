from http.client import HTTPResponse
from django.shortcuts import render
from django.http import HttpResponse
from warehouse.models import Warehouse, Product

# Create your views here.
def list_products(request):
    product_queryset = Product.objects.all()
    warehouse_queryset = Warehouse.objects.all()

    return render(request, 'list_everything.html', {'products': list(product_queryset), 'warehouses': list(warehouse_queryset)})
    #return HttpResponse("Hello World!")