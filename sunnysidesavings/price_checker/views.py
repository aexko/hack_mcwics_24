from django.shortcuts import render
from django.http import HttpResponse
# import requests

# Create your views here.
# def testing(request):
#     return HttpResponse("Hello, world. You're at the price_checker index.")

# return the index page
def priceCheckerPage(request):
    return render(request, "index.html")