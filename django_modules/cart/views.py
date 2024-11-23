from django.shortcuts import render
from django.http import JsonResponse
import json
# Create your views here.


def update_cart(request):
    data = json.loads(request.body.decode('utf-8'))
    product_id = data.get('productId')
    action = data.get('action')
    print('productId: ', product_id, 'action: ', action)
    return JsonResponse("data sent successfully", status=200)
