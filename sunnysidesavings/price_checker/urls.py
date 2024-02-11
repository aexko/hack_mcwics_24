# import some urls
from django.urls import path

from . import views

# create a list of urls
urlpatterns = [path("", views.priceCheckerPage, name="price_checker")]
