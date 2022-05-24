from django.urls import path
from . import views

urlpatterns = [
     path('list_everything/', views.list_products)
]