from django.shortcuts import render , redirect , HttpResponseRedirect
from store.models.customer import Customer
from django.views import  View

def Logout(request):
    request.session.clear()
    return redirect('homepage')