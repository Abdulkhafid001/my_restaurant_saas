from django.shortcuts import render, HttpResponse, redirect
from naija_kitchen.models import Restaurant, MenuCategory, MenuItem
from cart.models import Order


def get_admin_home(request):
    all_restaurants = Restaurant.objects.all()
    all_orders = Order.objects.all()
    all_menu = MenuCategory.objects.all()
    all_menu_items = MenuItem.objects.all()
    context = {'all_restaurants': all_restaurants, 'all_orders': all_orders,
               'all_menu': all_menu, 'all_menu_items': all_menu_items}
    return render(request, 'adminmain.html', context)


def add_order(request):
    pass


def add_menu_category(request):
    if request.method == 'POST':
        category_name = request.POST.get('category')
        restaurant = request.POST.get('restaurant')
        # print(category_name + "," + restaurant)

    return redirect('/naijakitchen/admin')


def add_menu_item(request):
    if request.method == 'POST':
        category = request.POST.get('category')
        name = request.POST.get('name')
        description = request.POST.get('description')
        price = request.POST.get('price')
        is_available = request.POST.get('is_available')
        image = request.FILES.get('item_image')
