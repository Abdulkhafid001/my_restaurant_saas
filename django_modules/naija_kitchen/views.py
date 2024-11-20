from django.shortcuts import redirect, render
from rest_framework import viewsets
from rest_framework import permissions
from naija_kitchen.forms import SignupForm, LoginForm
from django.contrib.auth import login as auth_login


from naija_kitchen.models import Restaurant, MenuCategory
from naija_kitchen.serializers import RestaurantSerializer, MenuCategorySerializer


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


def get_restaurant_menucategories(request):
    menu_categories = MenuCategory.objects.all()
    return render(request, 'menu_categories.html', {'menucategories': menu_categories})
