"""core URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from . import views


app_name = 'dashboard'

urlpatterns = [

    path('home/', views.DashboardView.as_view(), name='home'),
    path('check/', views.CheckView.as_view(), name='check'),
    path('deposits/', views.DepositsView.as_view(), name='deposits'),
    path('replenish/', views.Replenish.as_view(), name='replenish'),
    path('transactions/', views.TransactionsView.as_view(), name='transactions'),
    path('verification/', views.VerificationView.as_view(), name='verification'),
    path('verification2/', views.VerificationView2.as_view(), name='verification2'),
    path('settings/', views.SettingsView.as_view(), name='settings'),


]
