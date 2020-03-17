from django.urls import path

from . import views


app_name = 'main'
urlpatterns = [
    path('', views.index, name='index'),
    path('come_soon/', views.come_soon, name='come_soon'),
]