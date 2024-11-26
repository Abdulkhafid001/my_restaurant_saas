from .models import *
from django.http import HttpResponse
from cart import views
from naija_kitchen.models import Restaurant, MenuItem


def test(request):
    id = views.get_product_id_from_request(request)
    print(id)
    return HttpResponse(id)


def cart_data(request):
    if request.user.is_authenticated:
        user = request.user
        product_id = request.session.get('product_id_from_request')
        menu_item = MenuItem.objects.get(
            id=product_id)
        # menu_item = MenuItem.objects.get(
        #     id=views.get_product_id_from_request(request))
        restaurant = menu_item.category.restaurant
        order, created = Order.objects.get_or_create(
            user=user, restaurant=restaurant, defaults={"complete": False})
        items = order.orderitem_set.all()
        cart_items = order.get_cart_items
        return {'order': order, 'items': items, 'cartItems': cart_items}    
