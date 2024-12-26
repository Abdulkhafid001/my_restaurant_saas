from django.shortcuts import render, HttpResponse, redirect
from naija_kitchen.models import Restaurant, MenuCategory, MenuItem
from cart.models import Order

aba_restaurant = Restaurant.objects.get(restaurant_name='Aba Food Market')


def get_admin_home(request):
    all_restaurants = Restaurant.objects.all()
    all_orders = Order.objects.all()
    all_menu_category = MenuCategory.objects.all()
    all_menu_items = MenuItem.objects.all()
    menu_categories_for_aba = MenuCategory.objects.filter(
        restaurant=aba_restaurant)

    context = {'all_restaurants': all_restaurants, 'all_orders': all_orders,
               'all_menu': all_menu_category, 'all_menu_items': all_menu_items, 'categories_for_aba': menu_categories_for_aba,
               'items_count': count_items()}
    return render(request, 'adminmain.html', context)


def count_items():
    breakfast_category = MenuCategory.objects.filter(name="Breakfast").filter(restaurant=aba_restaurant)
    # lunch_category = MenuCategory.objects.filter(name="Lunch")
    # dinner_category = MenuCategory.objects.filter(name="Dinner")

    breakfast_count = MenuItem.objects.filter(category=breakfast_category).count()
    # lunch_count = MenuItem.objects.filter(category=lunch_category).count()
    # dinner_count = MenuItem.objects.filter(category=dinner_category).count()

    return {
        "breakfast_count": breakfast_count,
        # "lunch_count": lunch_count,
        # "dinner_count": dinner_count,
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
