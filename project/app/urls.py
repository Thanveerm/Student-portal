from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('register',views.register_api,name='register_api'),
    path('login',views.login,name='login'),




]
