from django.shortcuts import redirect, render, get_object_or_404, HttpResponse
from rest_framework import viewsets
from rest_framework import permissions
from .models import *
from .forms import SignupForm, LoginForm
from django.contrib.auth import login as auth_login
from .customencoder import DecimalEncoder
import json
from decimal import Decimal
from .serializers import RestaurantSerializer, MenuCategorySerializer


class RestaurantViewSet(viewsets.ModelViewSet):
    queryset = Restaurant.objects.all()
    serializer_class = RestaurantSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class MenuCategoryViewSet(viewsets.ModelViewSet):
    queryset = MenuCategory.objects.all()
    serializer_class = MenuCategorySerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


def get_cart_items_from_session(request):
    cart_items_in_session = request.session.get('cartItems')
    return cart_items_in_session


def get_all_restaurant(request):
    if request.user.is_authenticated:
        visit_count = request.session.get('visit_count', 0)
        visit_count += 1
        request.session['visit_count'] = visit_count
        cart_items = get_cart_items_from_session(request)
        restaurants = Restaurant.objects.all()
        restaurant_json = json.dumps(list(Restaurant.objects.values()))
        context = {'restaurants': restaurants,
                'visit_count': visit_count, 'cartItems': cart_items, 'restaurant_json': restaurant_json}
        return render(request, 'restaurant_list.html', context)
    else:
        return redirect('admin/')


def get_restaurant_menucategories(request, restaurant_slug):
    restaurant = get_object_or_404(Restaurant, slug=restaurant_slug)
    cart_items = get_cart_items_from_session(request)
    menu_categories = restaurant.menu_categories.all()
    context = {'restaurant': restaurant,
               'menucategories': menu_categories, 'cartItems': cart_items}
    return render(request, 'menu_categories.html', context)


def get_menucategory_items(request, restaurant_slug,  category_slug):
    restaurant = get_object_or_404(Restaurant, slug=restaurant_slug)
    category = get_object_or_404(
        MenuCategory, restaurant=restaurant, slug=category_slug)
    cart_items = get_cart_items_from_session(request)

    menu_items = MenuItem.objects.filter(category=category)
    menu_items_json = json.dumps(list(menu_items.values()), cls=DecimalEncoder)

    context = {'restaurant': restaurant,
               'category': category, 'menuitems': menu_items, 'cartItems': cart_items, 'menu_items_json': menu_items_json}
    return render(request, 'menu_items.html', context)
