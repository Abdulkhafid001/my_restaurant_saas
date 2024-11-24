from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
import json
# Create your views here.


def update_cart(request):
    if request.method == 'POST':
        data = json.loads(request.body.decode('utf-8'))
        product_id = data.get('productId')
        action = data.get('action')
        print('productId: ', product_id, 'action: ', action)
        # update cart logic here
        return JsonResponse("data sent successfully", safe=False, status=200)
    return JsonResponse({"error": "Invalid request"}, status=400)


def test_view(request):
    return HttpResponse("view works! perfectly")
