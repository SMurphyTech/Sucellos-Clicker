from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name="index"),  
    path('increase/', views.increase, name='increase'),
    path('decrease/', views.decrease, name='decrease'),
    path('update/', views.update, name='update')
]