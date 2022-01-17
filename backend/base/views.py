from re import I
from django.shortcuts import render
from django.http import JsonResponse
from .products import products

# Create your views here.


def getRoutes(request):
    return JsonResponse('hello', safe=False)

def getProducts(request):
    return JsonResponse(products,safe=False)