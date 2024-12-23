from django.shortcuts import render
from naija_kitchen.models import Restaurant, MenuCategory, MenuItem
from cart.models import Order


def get_admin_home(request):
    all_restaurants = Restaurant.objects.all()
    all_orders = Order.objects.all()
    all_menu = MenuCategory.objects.all()
    all_menu_items = MenuItem.objects.all()
    context = {'all_restaurants': all_restaurants, 'all_orders': all_orders,
               'all_menu': all_menu, 'all_menu_items': all_menu_items}
    return render(request, 'adminhome.html', context)
