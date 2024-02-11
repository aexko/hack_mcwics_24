from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

# return the index page
def priceCheckerPage(request):
    template = loader.get_template('index.html')
    return HttpResponse(template.render())