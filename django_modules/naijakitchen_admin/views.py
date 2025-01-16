import datetime
from django.utils import timezone
from django.utils.timezone import now
import json
from django.http import JsonResponse
from django.shortcuts import render, HttpResponse, redirect
from naija_kitchen.models import Restaurant, MenuCategory, MenuItem
from cart.models import Order

aba_restaurant = Restaurant.objects.get(restaurant_name='Aba Food Market')

today = now().date()
specific_date = datetime.date(2024, 12, 28)


filtered_orders = Order.objects.none()


def get_admin_home(request):
    menu_categories = MenuCategory.objects.filter(restaurant=aba_restaurant)
    menu_items = MenuItem.objects.filter(category__restaurant=aba_restaurant)
    context = {'restaurant': aba_restaurant, 'filtered_orders': get_filtered_orders(),
               'menu_items': menu_items, 'categories': menu_categories,
               'items_count': count_items(), 'order_status_count': get_order_status_count()}
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


def get_order_by_status_date(request):
    global filtered_orders
    if request.method == 'POST':
        data = json.loads(request.body)
        order_status = data.get('orderStatus')
        order_date = data.get('orderDate')
        print(order_status, order_date)
        # if order_status == '' | order_date == '':
        #     order_status = 'Preparing'
        #     order_date = timezone.now()
        filtered_orders = Order.objects.filter(
            status=order_status, date_ordered__date=order_date)
        return JsonResponse({'message': 'Order filter successful'}, safe=False)
        # return redirect('naijakitchenadminhome')
    return JsonResponse({'message': 'Invalid request method.'}, safe=False)


def get_filtered_orders():
    return filtered_orders


def get_order(request, order_id):
    order = Order.objects.get(id=order_id)
    order_items = order.orderitem_set.all()
    context = {'order': order, 'orderitems': order_items}
    return render(request, 'orderdetail.html', context)


def delete_order(request, order_id):
    order = Order.objects.get(id=order_id)
    if (order.DoesNotExist()):
        return JsonResponse({'message': 'order deleted successfully'}, safe=False)
    order.delete()
    redirect('naijakitchenadminhome')
    return JsonResponse({'message': 'order deleted successfully'}, safe=False)


def get_order_status_count():
    completed_count = Order.objects.filter(status='Completed').count()
    preparing_count = Order.objects.filter(status='Preparing').count()
    cancelled_count = Order.objects.filter(status='Cancelled').count()
    ready_count = Order.objects.filter(status='Ready').count()
    order_status_count = {'completed': completed_count, 'preparing': preparing_count,
                          'cancelled': cancelled_count, 'ready': ready_count}
    return order_status_count
