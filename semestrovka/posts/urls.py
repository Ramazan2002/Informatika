from django.urls import path
from . import views
urlpatterns = [
    path('create/', views.create, name='create_post'),
    path('<int:pk>', views.show.as_view(), name='post'),
    path('<int:pk>/update', views.update_post, name='update_post'),
    path('<int:pk>/delete', views.delete_post, name='delete_post'),
    path('post/ajax/comment/<int:pk>', views.create_comment, name='create_comment'),
]