from django.shortcuts import render



# Create your views here.

def home(request):
    return render(request, 'pages/index.html')

def about(request):
    return render(request, 'pages/about.html')


def contact(request):
    return render(request, 'pages/contact.html')

def room(request):
    return render(request, 'pages/room.html')



def singleroom(request):
    return render(request, 'pages/single-room.html')
