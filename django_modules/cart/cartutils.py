from .models import *
from cart import views
from naija_kitchen.models import Restaurant, MenuItem


def cart_data(request):
    if request.user.is_authenticated:
        user = request.user
        menu_item = MenuItem.objects.get(id=views.get_product_id(5))
        restaurant = menu_item.category.restaurant
        order, created = Order.objects.get_or_create(
            user=user, restaurant=restaurant, defaults={"complete": False})
        items_in_order = order.orderitem_set.all()
        cart_items = order.get_cart_items
        return {'order': order, 'items': items_in_order, 'cartItems': cart_items}