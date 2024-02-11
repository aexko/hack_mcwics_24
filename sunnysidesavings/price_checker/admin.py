from django.contrib import admin
from .models import GroceryItem, GroceryStore

# GroceryItem and GroceryStore are registered with the admin site
admin.site.register(GroceryItem)
admin.site.register(GroceryStore)
