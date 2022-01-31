from django.shortcuts import render


def home(render):
    return render(request, 'home.html')

def room(render):
    return render(request, 'room.html')