import csv

from datetime import datetime
from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.views.decorators.http import require_POST
from django.db.models import Q
from .models import Customer
from .forms import CustomerForm

# View to display list of customers
@login_required
def customers_list(request):
    query = request.GET.get('q')
    date_from = request.GET.get('from')
    date_to = request.GET.get('to')

    customers = Customer.objects.all()

    if query:
        customers = customers.filter(
            Q(name__icontains=query) |
            Q(email__icontains=query) |
            Q(cpf__icontains=query)
        )

    if date_from:
        customers = customers.filter(registration_date__gte=date_from)
    if date_to:
        customers = customers.filter(registration_date__lte=date_to)

    return render(request, 'customers/customers_list.html', {'customers': customers})

# View to create a new customer
@login_required
def create_customer(request):
    if request.method == 'POST':
        form = CustomerForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('customers_list')
    else:
        form = CustomerForm()
    return render(request, 'customers/create_customer.html', {'form': form})

@login_required
@require_POST
def delete_customer(request, pk):
    customer = get_object_or_404(Customer, pk=pk)
    customer.delete()
    return redirect('customers_list')

@login_required
def edit_customer(request, pk):
    customer = get_object_or_404(Customer, pk=pk)
    
    if request.method == 'POST':
        form = CustomerForm(request.POST, instance=customer)
        if form.is_valid():
            form.save()
            return redirect('customers_list')
    else:
        form = CustomerForm(instance=customer)

    return render(request, 'customers/edit_customer.html', {'form': form, 'customer': customer})

@login_required
def customer_detail(request, pk):
    customer = get_object_or_404(Customer, pk=pk)
    return render(request, 'customers/customer_detail.html', {'customer': customer})
