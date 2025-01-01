import datetime
from django.utils import timezone
import json
from django.http import JsonResponse
from django.shortcuts import render, HttpResponse, redirect
from naija_kitchen.models import Restaurant, MenuCategory, MenuItem
from cart.models import Order

aba_restaurant = Restaurant.objects.get(restaurant_name='Aba Food Market')

filtered_orders = Order.objects.none()

def get_admin_home(request):
    filtered_orders = Order.objects.filter(
        status='Preparing', date_ordered__gte=timezone.now)[:1]
    menu_categories = MenuCategory.objects.filter(restaurant=aba_restaurant)
    menu_items = MenuItem.objects.filter(category__restaurant=aba_restaurant)
    context = {'restaurant': aba_restaurant, 'filtered_orders': filtered_orders,
               'menu_items': menu_items, 'categories': menu_categories,
               'items_count': count_items()}
    return render(request, 'adminmain.html', context)


def count_items():
    breakfast_category = MenuCategory.objects.filter(
        name="Breakfast").filter(restaurant=aba_restaurant).first()
    lunch_category = MenuCategory.objects.filter(
        name="Lunch").filter(restaurant=aba_restaurant).first()
    dinner_category = MenuCategory.objects.filter(
        name="Dinner").filter(restaurant=aba_restaurant).first()

    breakfast_count = MenuItem.objects.filter(
        category=breakfast_category).count()
    lunch_count = MenuItem.objects.filter(category=lunch_category).count()
    dinner_count = MenuItem.objects.filter(category=dinner_category).count()

    return {
        "breakfast_count": breakfast_count,
        "lunch_count": lunch_count,
        "dinner_count": dinner_count,
    }


def add_order(request):
    pass


def add_menu_category(request):
    if request.method == 'POST':
        category_name = request.POST.get('category')
        restaurant_name = request.POST.get('restaurant_name')
        description = request.POST.get('description')
        category_image = request.FILES.get('category_image')
        if MenuCategory.objects.filter(name=category_name).exists():
            return HttpResponse("<p>exits please try another</p><a href='http://127.0.0.1:8000/naijakitchen/admin/'>go back home</a>")
        else:
            if Restaurant.objects.filter(restaurant_name=str(restaurant_name)).exists():
                restaurant = Restaurant.objects.get(
                    restaurant_name=restaurant_name)
                MenuCategory.objects.create(
                    restaurant=restaurant, name=category_name, description=description, image=category_image)
            return HttpResponse("<p>Category added successfully</p><a href='http://127.0.0.1:8000/naijakitchen/admin/'>go back home</a>")


def add_menu_item(request):
    if request.method == 'POST':
        category = request.POST.get('category')
        restaurant_name = request.POST.get('restaurant_name')
        item_name = request.POST.get('name')
        description = request.POST.get('description')
        price = request.POST.get('price')
        is_available = request.POST.get('available')
        image = request.FILES.get('image')

        if is_available == 'on':
            is_available = True
        else:
            is_available = False

        restaurant = Restaurant.objects.get(restaurant_name=restaurant_name)
        item_category = MenuCategory.objects.get(
            restaurant=restaurant, name=category)
        if MenuItem.objects.filter(name=item_name).exists():
            return HttpResponse("<p>exits please try another</p><a href='http://127.0.0.1:8000/naijakitchen/admin/'>go back home</a>")
        else:
            if MenuCategory.objects.filter(name=category).exists():
                MenuItem.objects.create(
                    category=item_category, name=item_name, description=description, price=price, is_available=is_available, image=image
                )
                pass
            return HttpResponse("<p>Item added successfully</p><a href='http://127.0.0.1:8000/naijakitchen/admin/'>go back home</a>")


def order_get(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        order_status = data.get('orderStatus')
        order_date = data.get('orderDate')
        # print(order_status, order_date)
        if order_status == '' | order_date == '':
            order_status = 'Preparing'
            order_date = timezone.now()
        filtered_orders = Order.objects.filter(
            status=order_status, date_ordered=order_date)
        return JsonResponse({'filtered_orders': list(filtered_orders.values())}, safe=False)
    return JsonResponse({'message': 'Invalid request method.'}, safe=False)
