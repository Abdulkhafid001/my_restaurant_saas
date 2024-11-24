from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
import json
from .models import *
from naija_kitchen.models import MenuItem


def update_cart(request):
    if request.method == 'POST':
        data = json.loads(request.body.decode('utf-8'))
        product_id = data.get('productId')
        action = data.get('action')

        customer = request.user
        menu_item = MenuItem.objects.get(id=product_id)

        print('customer: ', customer, 'menu item: ', menu_item)
        # order, created = Order.objects.get_or_create(user=customer)
        # update cart logic here
        return JsonResponse("data sent successfully", safe=False, status=200)
    return JsonResponse({"error": "Invalid request"}, status=400)
