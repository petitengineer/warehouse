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
        print("it was a get")
        print(request.body)
        product_queryset = Product.objects.all()
        warehouse_queryset = Warehouse.objects.all()

        return render(request, 'list_everything.html', {'products': list(product_queryset), 'warehouses': list(warehouse_queryset)})

        ##################################
    elif request.method == 'POST': #Create
        data = request.body
        json_data = json.loads(data.decode("utf-8").replace("'",'"'))
        print("~~~~The dictionary: ", json_data)
        create(json_data)

        print("it was a post")
    elif request.method == 'PUT': #Update
        print("Here's your data \n")
        data = request.body
        json_data = json.loads(data.decode("utf-8").replace("'",'"'))
        update(json_data)
        print("it was a put")
    elif request.method == 'DELETE': #Delete
        data = request.body
        json_data = json.loads(data.decode("utf-8").replace("'",'"'))
        delete(json_data)
        print("successfully deleted")
    else:
        print("ERROR: COMMAND NOT RECOGNIZED.")

    
    return HttpResponse("Command executed successfully!\n")

def create(data):
    try:
        data_type = data.pop('type')
        if data_type == 'Warehouse':
            Warehouse.objects.create(**data)
        elif data_type == 'Product':
            Product.objects.create(**data)
            print('product was created!')
    except:
            print('Data was mislabled or invalid.')

def update(data):
    try:
        data_type = data.pop('type')
        if data_type == 'Warehouse':
            print("updating warehouse data")
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