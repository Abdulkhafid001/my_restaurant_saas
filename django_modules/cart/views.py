from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
import json
from .models import *
from .cartutils import cart_data
from naija_kitchen.models import MenuItem


product_id_from_request = 0


def update_cart(request):
    print("view called!")
    if request.method == 'POST':
        data = json.loads(request.body.decode('utf-8'))
        product_id = data.get('productId')
        action = data.get('action')
        product_id_from_request = product_id
        user = request.user
        menu_item = MenuItem.objects.get(id=product_id)
        restaurant = menu_item.category.restaurant

        print(user, 'has ordered : ', menu_item, ' from: ', restaurant)

        order, created = Order.objects.get_or_create(
            user=user, restaurant=restaurant, defaults={"complete": False})
        order_item, created = OrderItem.objects.get_or_create(
            product=menu_item, order=order
        )

        print(f'User: {user}, Restaurant: {restaurant}, Order Created: {created}')

        if action == 'add':
            order_item.quantity = (order_item.quantity + 1)
        elif action == 'remove':
            order_item.quantity = (order_item.quantity - 1)

        order_item.save()

        if order_item.quantity <= 0:
            order_item.delete()
        return JsonResponse("data sent successfully", safe=False, status=200)
    return JsonResponse({"error": "Invalid request try another!"}, status=400)


def cart(request):
    if request.user.is_authenticated:
        user = request.user
        order = Order.objects.filter(user=user)
        items_in_order = order.orderitems.all()
        cart_items = order.get_cart_items
        context = {'order': order, 'items': items_in_order,
                   'cartItems': cart_items}
    return render(request, 'cart.html', context)


def checkout(request):
    pass


def get_product_id_from_request():
    return product_id_from_request
