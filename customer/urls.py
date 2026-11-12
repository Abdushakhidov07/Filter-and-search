from .views import *
from django.urls import path

urlpatterns = [
    path("add_customer/", add_customer, name='add_customers'),
    path("get_customer/", get_customer, name='show_customers')
]
