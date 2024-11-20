import json
from naija_kitchen.models import MenuCategory, MenuItem
from django.shortcuts import render
from django.views.generic import ListView


class MenuCategoriesListView(ListView):
    model = MenuCategory
    template_name = 'menu_category.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['qs_json'] = json.dumps(list(MenuCategory.objects.values()))
        return context
