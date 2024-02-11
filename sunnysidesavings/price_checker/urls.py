# import some urls
from django.urls import path

from . import views


# create a list of urls
urlpatterns = [
    path("", views.price_checker_render, name="price_checker"),
    path("get_grocery_items", views.get_grocery_items, name="get_grocery_items"),
    path("get_grocery_items_by_name", views.get_grocery_items_by_name, name="get_grocery_items_by_name"),
    path("get_grocery_items_by_grocery_stores", views.get_grocery_items_by_grocery_stores, name="get_grocery_items_by_grocery_stores"),]
