from django.shortcuts import render
from django.http import HttpResponse
from .models import GroceryItem, GroceryStore


# rendering a list of grocery items
def price_checker_render(request):
    return render(request, "index.html")

# return all grocery items
def get_grocery_items(request):
    grocery_items = GroceryItem.objects.all()
    print(grocery_items)
    return HttpResponse(grocery_items)

# filtering grocery items by name that user inputs
def get_grocery_items_by_name(request):
    grocery_items = GroceryItem.objects.all()
    print(grocery_items)
    print("request", request)
    print("request.GET", request.GET)
    return ""


# rendering a list of grocery items by grocery stores
def get_grocery_items_by_grocery_stores(request):
    grocery_items = GroceryItem.objects.filter(grocery_store__name__icontains=request.GET["name"])
    print(grocery_items)
    return HttpResponse(grocery_items)

