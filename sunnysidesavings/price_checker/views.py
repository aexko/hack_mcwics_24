from django.shortcuts import render
from .models import GroceryItem, GroceryStore


# Function to simply render the index.html page
def price_checker_render(request):
    grocery_items = GroceryItem.objects.all()
    context = {"grocery_items": grocery_items}
    return render(request, "index.html", context)



# Function that gets the grocery items based on the user input in the
# search bar, and it is based the the name of the grocery item
def get_grocery_items_by_name(request):
    if request.method == "GET":
        grocery_item_name = request.GET["grocery_item_name"]
        grocery_items = GroceryItem.objects.filter(name__icontains=grocery_item_name)
        context = {"grocery_items": grocery_items}
        return render(request, "index.html", context)
    return render(request, "index.html")


# Function that gets the grocery items based on the user input in the
# search bar, and it is based the the name of the grocery store
def get_grocery_items_by_grocery_stores(request):
    if request.method == "GET":
        grocery_store_name = request.GET["grocery_store_name"]
        grocery_items = GroceryItem.objects.filter(grocery_store__name__icontains=grocery_store_name)
        context = {"grocery_items": grocery_items}
        return render(request, "index.html", context)
    return render(request, "index.html")
