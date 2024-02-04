from django.urls import path, re_path, include
from . import views

urlpatterns = [
    path('', views.index),
    path('week/', views.weekweather),
    path('outfits/', views.outfits),
    path('register/', views.register),
    path('support/', views.support),
    path('feedback/', views.feedback),
    path('ready/', views.readyout),
    path('looks/', views.looks)

]
