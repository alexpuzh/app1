from django.shortcuts import render
from django.shortcuts import HttpResponse


def catalog(request) -> HttpResponse:
    return render(request, 'goods/catalog.html')


def product(request) -> HttpResponse:
    return render(request, 'goods/product.html')

