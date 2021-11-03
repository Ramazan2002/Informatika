from django.urls import path
from . import views

urlpatterns = [
    path('', views.main, name='main'),
    path('register/', views.register, name='register'),
    path('login/', views.login, name='login'),
    path('profile/<int:pk>', views.profile, name='profile'),
    path('profile/settings', views.profile_settings, name='profile_settings'),
    path('profile/<int:pk>/posts', views.profile_posts, name='profile_posts'),
    path('logout/', views.logout, name='logout'),
]
