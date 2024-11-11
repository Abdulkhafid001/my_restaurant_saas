from django.shortcuts import render
from naija_kitchen.models import *
# Create your views here.


def get_names(request):
    all_names = Person.objects.all()
    return render(request, 'signup.html', {'all_names': all_names})
