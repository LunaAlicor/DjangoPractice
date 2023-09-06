from django.shortcuts import render
from django.contrib.auth.models import Group
from .models import Product
# Create your views here.


def index(request):
    return render(request, 'shopaap/index.html')


def shop(request):
    return render(request, 'shopaap/shop.html')


def group_list(request):
    context = {
        'groups': Group.objects.prefetch_related('permissions').all(),
    }
    return render(request, 'shopaap/group-list.html', context=context)


def product_list(request):
    context = {
        "products": Product.objects.all(),
    }
    return render(request, 'shopaap/product-list.html', context=context)