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
        print("it was a delete")
    else:
        print("ERROR: COMMAND NOT RECOGNIZED.")

    
    return HttpResponse("Hello World!")

def create(data):
    try:
        if data['type'] == 'Warehouse':
            warehouse = Warehouse()
            warehouse.name = data['name']
            warehouse.save()
        elif data['type'] == 'Product':
            product = Product()
            product.title = data['title']
            product.slug = data['slug']
            product.description = data['description']
            product.unit_price = data['unit_price']
            product.inventory = data['inventory']
            product.last_update = data['last_update']
            product.shelving_unit = data['shelving_unit']
            product.warehouse = data['warehouse_id']
            product.save()
    except:
            print('Data was mislabled or invalid.')

def update(data):
    #key_list = data.keys()
    #try:
        data_type = data.pop('type')
        if data_type == 'Warehouse':
            #warehouse = Warehouse.objects.get(pk=data.pop('id'))
            print("updating warehouse data")
            Warehouse.objects.filter(pk=data.pop('id')).update(**data)
            
            #for key in key_list:
            #    warehouse.key = data[key]
            #warehouse.save()
        elif data_type == 'Product':
            #product = Product.objects.get(pk=data.pop('id'))
            Product.objects.filter(pk=data.pop('id')).update(**data)
            #product.save()
    #except:
    #        print('Data was mislabled or invalid.')
