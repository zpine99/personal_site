from django.urls import path

from . import views


app_name = 'main'
urlpatterns = [
    path('', views.index, name='index'),
    path('come_soon/', views.come_soon, name='come_soon'),
    path('about_me/', views.about_me, name='about_me'),
    path('advice/', views.advice, name='advice'),
]