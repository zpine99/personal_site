from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import Advice 


def index(request):
    return render(request, 'main/index.html')


def come_soon(request):
    return render(request, 'main/come_soon.html')


def about_me(request):
    return render(request, 'main/about_me.html')


def advice(request):
    if request.method == 'POST':
        message = Advice(name=request.POST['name'],
                         email=request.POST['email'],
                         advice=request.POST['message'])
        message.save()                        
    return HttpResponseRedirect(reverse('main:about_me', ))