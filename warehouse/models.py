from pydoc import describe
from django.db import models

class Collection(models.Model):
    name = models.CharField(max_length=255)

class Warehouse(models.Model):
    name = models.CharField(max_length=255) 

class Product(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(default="-")
    description = models.TextField()
    unit_price = models.DecimalField(max_digits = 6, decimal_places=2)
    inventory = models.IntegerField()
    last_update = models.DateTimeField(auto_now = True) #indicates date-time of last edit
    shelving_unit =  models.CharField(max_length=3)
    collection = models.ForeignKey(Collection, on_delete=models.PROTECT)
    warehouse = models.ForeignKey(Warehouse, on_delete=models.PROTECT, null=True)
    
#Maybe add if time allows:
#class Address(models.Model):
#    street_address = models.TextField(max_length=255)
#    zip_code = models.TextField(max_length=10, default='ERROR')
#    unit_number = models.IntegerField()
#    city_name = models.TextField(max_length=255)
#    country_or_province = models.TextField(max_length=255)
#    country = models.TextField(max_length=255)
#    warehouse = models.OneToOneField(Warehouse, on_delete=models.CASCADE, primary_key=True)