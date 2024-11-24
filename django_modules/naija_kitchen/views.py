from django.shortcuts import redirect, render, get_object_or_404
from rest_framework import viewsets
from rest_framework import permissions
from .models import *
from cart.views import update_cart
from .forms import SignupForm, LoginForm
from django.contrib.auth import login as auth_login
from .serializers import RestaurantSerializer, MenuCategorySerializer


class RestaurantViewSet(viewsets.ModelViewSet):
    queryset = Restaurant.objects.all()
    serializer_class = RestaurantSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class MenuCategoryViewSet(viewsets.ModelViewSet):
    queryset = MenuCategory.objects.all()
    serializer_class = MenuCategorySerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request, user)
            return redirect('api-home')
    else:
        form = SignupForm()
    return render(request, 'signup.html', {'signupForm': form})


def login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            user = form.cleaned_data['user']
            auth_login(request, user)  # Log in the user
            return redirect('api-home')  # Redirect to your desired page
    else:
        form = LoginForm()
    return render(request, "login.html", {'loginForm': form})


def get_all_restaurant(request):
    visit_count = request.session.get('visit_count', 0)
    visit_count += 1
    request.session['visit_count'] = visit_count
    restaurants = Restaurant.objects.all()
    context = {'restaurants': restaurants, 'visit_count': visit_count}
    return render(request, 'restaurant_list.html', context)


def get_restaurant_menucategories(request, slug):
    restaurant = get_object_or_404(Restaurant, slug=slug)
    menu_categories = restaurant.menu_categories.all()
    context = {'restaurant': restaurant, 'menucategories': menu_categories}
    return render(request, 'menu_categories.html', context)


def get_menucategory_items(request, restaurant_slug,  category_slug):
    restaurant = get_object_or_404(Restaurant, slug=restaurant_slug)
    category = get_object_or_404(
        MenuCategory, slug=category_slug, restaurant=restaurant)
    menu_items = MenuItem.objects.filter(category=category)
    context = {'restaurant': restaurant,
               'category': category, 'menuitems': menu_items}
    return render(request, 'menu_items.html', context)
