from django.shortcuts import render, HttpResponse



def test_server(request):
    return HttpResponse("App configured properly!")
