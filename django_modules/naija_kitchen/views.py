from django.shortcuts import render
from naija_kitchen.models import *
from django.views.generic import ListView
# Create your views here.


class RestaurantListView(ListView):
    model = Restaurant
    template_name = 'restaurant_list.html'
