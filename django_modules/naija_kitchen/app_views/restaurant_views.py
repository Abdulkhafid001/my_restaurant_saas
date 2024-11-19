from django_modules.naija_kitchen.models import Restaurant
from django.shortcuts import render


def get_all_restaurants(request):
    all_restaurants = Restaurant.objects().all()
    return render(request, 'restuarant_list.html', {'all_restaurants': all_restaurants})
