from django.shortcuts import render

# Create your views here.


def room(request):
    return render(request, 'pages/room.html')

def singleroom(request):
    return render(request, 'pages/single-room.html')