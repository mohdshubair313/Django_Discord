from django.shortcuts import render
from models import Room
# Create your views here.

def home(request):
    rooms = Room.objects.all()
    context = {'rooms': rooms}
    return render(request, '', context)
    # return render(request, 'base/home.html', context)

def room(request):
    return render(request, '')