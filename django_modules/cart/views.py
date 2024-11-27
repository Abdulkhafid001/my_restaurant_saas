from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
import json
from .models import *
from .cartutils import cart_data
from naija_kitchen.models import MenuItem
import datetime



def update_cart(request):
    print("view called!")
    if request.method == 'POST':
        data = json.loads(request.body.decode('utf-8'))
        product_id = data.get('productId')
        action = data.get('action')
        request.session['product_id_from_request'] = product_id
        user = request.user
        menu_item = MenuItem.objects.get(id=product_id)
        restaurant = menu_item.category.restaurant

        print(user, 'has ordered : ', menu_item, ' from: ', restaurant)

        order, created = Order.objects.get_or_create(
            user=user, restaurant=restaurant, complete = False)
        order_item, created = OrderItem.objects.get_or_create(
            product=menu_item, order=order
        )
        request.session['cartItems'] = int(order.get_cart_items)

        print(f'User: {user}, Restaurant: {restaurant}, Order Created: {created}')

        if action == 'add':
            order_item.quantity = (order_item.quantity + 1)
        elif action == 'remove':
            order_item.quantity = (order_item.quantity - 1)

        order_item.save()

        if order_item.quantity <= 0:
            order_item.delete()
        return JsonResponse("data sent successfully", safe=False, status=200)
    return JsonResponse({"error": "Invalid request try another!"}, safe=False, status=400)


def get_product_id_from_request(request):
    return request.session.get('product_id_from_request')


def cart(request):
    if request.user.is_authenticated:
        data = cart_data(request)
        order = data['order']
        items = data['items']
        cart_items = data['cartItems']
        context = {'order': order, 'items': items, 'cartItems': cart_items}
        return render(request, 'cart.html', context)


def checkout(request):
    if request.user.is_authenticated:
        data = cart_data(request)
        order = data['order']
        items = data['items']
        cart_items = data['cartItems']
        context = {'order': order, 'items': items, 'cartItems': cart_items}
        return render(request, 'checkout.html', context)


def process_order(request):
    # REMEMBER TO CLEAR PRODUCT_ID SESSION / OR FULL SESSON  IF ORDER IS COMPLETED
    transaction_id = datetime.datetime.now().timestamp()
    frontend_data = json.loads(request.body.decode('utf-8'))

    user_name = frontend_data['userInfo']['name']
    user_phone = frontend_data['userInfo']['phoneNumber']
    user_delivery_address = frontend_data['userInfo']['deliveryAddress']
    cart_total = float(frontend_data['userInfo']['total'])
    print(user_name, user_phone, user_delivery_address, cart_total)

    if request.user.is_authenticated:
        user = request.user
        product_id = request.session.get('product_id_from_request')
        menu_item = MenuItem.objects.get(
            id=product_id)
        restaurant = menu_item.category.restaurant
        order, created = Order.objects.get_or_create(
            user=user, restaurant=restaurant, complete=False
        )

    order.transaction_id = transaction_id
    if cart_total == order.get_cart_total:
        order.complete = True
        order.save()
        del request.session['product_id_from_request']
        del request.session['cartItems']

    return JsonResponse({'message': 'Order being processed..'}, safe=False, status=200)
