from django.shortcuts import render

from . models import *

# Create your views here.


def contact(request):
    email = Contact.objects.all()
    name = Contact.objects.all()
    message = Contact.objects.all()
    
    email = request.POST.get('email')
    name = request.POST.get('name')
    message = request.POST.get('message')
    
    if name is not None and email is not None and message is not None:
        me = Contact(name=name, email=email, message=message)
        me.save()
    
    context = { "email": email, "name": name, "message": message}
    return render(request, 'pages/contact.html', context)
