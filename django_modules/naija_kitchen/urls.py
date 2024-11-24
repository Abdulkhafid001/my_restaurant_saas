from django.urls import include, path
from .views import *
from .app_views.restaurant_views import RestaurantListView
from cart.views import update_cart

from rest_framework.routers import DefaultRouter
router = DefaultRouter()
router.register(r'restaurants', RestaurantViewSet)
router.register(r'menucategories', MenuCategoryViewSet)

urlpatterns = [
    # path('', include(router.urls), name='api-home'),
    path('login/', login, name='login'),
    path('signup/', signup, name='signup'),
    path("", get_all_restaurant, name="all_restaurants"),
    # path("<slug:slug>/", get_restaurant_menucategories, name="restaurant_menucategories"),
    path('<slug:restaurant_slug>/<slug:category_slug>/', get_menucategory_items, name="restaurant_menuitems"),
    path("update_cart/", update_cart, name="update_cart"),
] 
 