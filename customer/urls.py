from .views import *
from django.urls import path

urlpatterns = [
    path("create_order/<int:pk>", create_order, name='create_order'),
    path("get_products/", get_products, name='get_products')
]
