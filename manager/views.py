from django.shortcuts import render
from .models import Manager
# Create your views here.

def manager_list(request):
    manager = Manager.objects.all()

    return render(request, 'back/manager_list.html', {'manager':manager})