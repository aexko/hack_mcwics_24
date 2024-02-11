# import some urls
from django.urls import path
from . import views

urlpatterns = [
    path("", views.price_checker_render, name="price_checker"),
    # class views for the grocery items
    path(
        "search_grocery_items",
        views.GroceryItemView.as_view(),
        name="search_grocery_items",
    ),
    # path("get_grocery_items", views.get_grocery_items, name="get_grocery_items"),
    path(
        "get_grocery_items_by_name",
        views.GroceryItemView.as_view(),
        name="get_grocery_items_by_name",
    ),
]
