from django.shortcuts import render, redirect
from .models import *
from django.db.models import Q

# Create your views here.

def add_customer(request):
    if request.method == "POST":
        data = request.POST
        Customer.objects.create(
            fullname = data['fullname'],
            age = data['age'],
            phone = data['phone'],
            email = data['email']
        )
        return redirect('show_customers')
    return render(request, 'add_customer.html')
    
    
def get_customer(request):
    
    query = request.GET.get('q')
    customers=Customer.objects.all()
    if query:
        customers=customers.filter(
            fullname__icontains = query
        )

    return render(request, 'show_customer.html', {"customers":customers, 'query':query})
        