from django.shortcuts import render, HttpResponse
from django.contrib.auth.models import AbstractUser


def test_server(request):
    
    return render(request, 'auths.html')
