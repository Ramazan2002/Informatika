"""infa_django URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.urls import path
from firstapp.views import main, profile, news, change_profile, delete_profile

urlpatterns = [
    path('main/', main, name='main'),
    path('profile/', profile, name='profile'),
    path('news/', news, name='news'),
    path('profile/<int:pk>/change', change_profile, name='change_profile'),
    path('profile/<int:pk>/delete', delete_profile, name='delete_profile')
]