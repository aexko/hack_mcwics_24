from django.shortcuts import render
from django.http import HttpResponse
from .models import GroceryItem, GroceryStore
from django.views.generic import ListView


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
    print("request", request.GET["search"])
    return HttpResponse(grocery_items)


# class view for the grocery items, it shows all the grocery items filtered by the name
class GroceryItemView(ListView):
    model = GroceryItem
    template_name = "grocery_items.html"
    context_object_name = "grocery_items"

    def get_queryset(self):
        query = self.request.GET.get("search")
        print("query: ", query)
        print("things returned: ", GroceryItem.objects.filter(name__icontains=query).order_by("price_per_unit"))
        return GroceryItem.objects.filter(name__icontains=query).order_by("price_per_unit")
