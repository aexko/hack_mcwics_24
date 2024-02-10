# import some urls
from django.urls import path
# import views from price_checker
from . import views

# create a list of urls
urlpatterns = [
    path('', views.testing, name='testing'),
]