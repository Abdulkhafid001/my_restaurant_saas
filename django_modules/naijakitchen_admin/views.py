from django.shortcuts import render
from django.shortcuts import HttpResponse
# Create your views here.

def get_admin_home(request):
    return HttpResponse("Start building admin here!")
