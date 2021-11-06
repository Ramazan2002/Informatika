from django.urls import path, re_path
from . import views

urlpatterns = [
    path('', views.main, name='main'),
    re_path(r'^admin/(?P<pk>[0-9]+)/$', views.admin_update, name='admin_update'),
    re_path(r'^admin/$', views.admin, name='admin'),
    path('register/', views.register, name='register'),
    path('login/', views.login, name='login'),
    path('profile/<int:pk>', views.profile, name='profile'),
    path('profile/settings', views.profile_settings, name='profile_settings'),
    path('profile/<int:pk>/posts', views.profile_posts, name='profile_posts'),
    path('logout/', views.logout, name='logout'),
]
