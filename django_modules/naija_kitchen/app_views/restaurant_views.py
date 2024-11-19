import json
from naija_kitchen.models import Restaurant
from django.shortcuts import render
from django.views.generic import ListView


class RestaurantListView(ListView):
    model = Restaurant
    template_name = 'restaurant_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['qs_json'] = json.dumps(list(Restaurant.objects.values()))
        return context
