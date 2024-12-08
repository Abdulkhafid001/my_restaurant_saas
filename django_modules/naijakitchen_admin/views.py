from django.shortcuts import render
from django.shortcuts import HttpResponse
from naija_kitchen.models import Restaurant
from cart.models import Order
def get_admin_home(request):
    all_restaurants = Restaurant.objects.all()
    all_orders = Order.objects.all()
    context = {'all_restaurants': all_restaurants, 'all_orders': all_orders}
    return render(request, 'adminhome.html', context)
