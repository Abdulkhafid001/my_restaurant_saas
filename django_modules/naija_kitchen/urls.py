from django.urls import include, path
from naija_kitchen import views
from naija_kitchen.app_views.restaurant_views import RestaurantListView
from cart import views as cart_views

from rest_framework.routers import DefaultRouter
router = DefaultRouter()
router.register(r'restaurants', views.RestaurantViewSet)
router.register(r'menucategories', views.MenuCategoryViewSet)

urlpatterns = [
    # path('', include(router.urls), name='api-home'),
    path('login/', views.login, name='login'),
    path('signup/', views.signup, name='signup'),
    path("", views.get_all_restaurant, name="all_restaurants"),
    path("<slug:slug>/", views.get_restaurant_menucategories, name="restaurant_menucategories"),
    path('<slug:restaurant_slug>/<slug:category_slug>/', views.get_menucategory_items, name="restaurant_menuitems"),
    path("update_cart/", cart_views.update_cart, name="update_cart")
] 
 