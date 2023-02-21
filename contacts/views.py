from django.shortcuts import render , redirect
import datetime
from django.contrib import messages
from django.http import HttpResponse
from django.urls import reverse
from .models import Contact

from django.template import RequestContext

def contact(request):
    if request.method == "POST":
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        message = request.POST['message']
        contact_date = datetime.datetime.now()



        contact = Contact(name=name, email=email, phone=phone, message=message,contact_date=contact_date)
        contact.save()

        messages.success(request,
                         'you have new messages! ')
    context = {
    }
    return render(request, 'store/contact.html', context)

    #return render('store/contact.html',
        #context_instance=RequestContext(request))
