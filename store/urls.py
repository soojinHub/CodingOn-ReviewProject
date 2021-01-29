from django.urls import path, include
from django.contrib.auth import views as auth_views
from. import views

urlpatterns = [
    path('',views.index),
    path('index/',views.index, name='index'),
    path('menu/',views.menu),
    path('review/',views.review),
    path('info/',views.info),
    path('purchase', views.purchase)
         ]

