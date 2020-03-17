from django.shortcuts import render


def index(request):
    return render(request, 'main/index.html')


def come_soon(request):
    return render(request, 'main/come_soon.html')


def about_me(request):
    return render(request, 'main/about_me.html')