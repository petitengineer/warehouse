from http.client import HTTPResponse
from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from warehouse.models import Warehouse, Product
import json #from python

# Create your views here.
@csrf_exempt
def list_products(request):
    if request.method == 'GET': #View
        product_queryset = Product.objects.all()
        warehouse_queryset = Warehouse.objects.all()
        return render(request, 'list_everything.html', {'products': list(product_queryset), 'warehouses': list(warehouse_queryset)})

    elif request.method == 'POST': #Create
        data = request.body
        json_data = json.loads(data.decode("utf-8").replace("'",'"'))
        create(json_data)
        return HttpResponse("Successfully added the following to the database: \n" + str(json_data))

    elif request.method == 'PUT': #Update
        data = request.body
        json_data = json.loads(data.decode("utf-8").replace("'",'"'))
        update(json_data)
        return HttpResponse("Successfully modified the following in the database: \n" + str(json_data))

    elif request.method == 'DELETE': #Delete
        data = request.body
        json_data = json.loads(data.decode("utf-8").replace("'",'"'))
        delete(json_data)
        return HttpResponse("Successfully modified the following in the database: \n" + str(json_data))

    else:
        return HttpResponse("ERROR: COMMAND NOT RECOGNIZED! \n")

def create(data):
    try:
        data_type = data.pop('type')
        if data_type == 'Warehouse':
            Warehouse.objects.create(**data)
        elif data_type == 'Product':
            Product.objects.create(**data)
    except:
        print('Data was mislabled or invalid.')

def update(data):
    try:
        data_type = data.pop('type')
        if data_type == 'Warehouse':
            Warehouse.objects.filter(pk=data.pop('id')).update(**data)            
        elif data_type == 'Product':
            Product.objects.filter(pk=data.pop('id')).update(**data)
    except:
        print('Data was mislabled or invalid.')

def delete(data):
    try:
        data_type = data.pop('type')
        if data_type == 'Warehouse':
            Warehouse.objects.filter(pk=data.pop('id')).delete()            
        elif data_type == 'Product':
            Product.objects.filter(pk=data.pop('id')).delete()
    except:
            print('Data was mislabled or invalid.')