from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('posts/', views.posts, name='posts'),
    path('posts/<str:id>/', views.single_post, name='single_post'),
    path('create_post/', views.create_post, name='create_post'),
    path('edit_post/<str:id>/', views.edit_post, name='edit_post'),
    path('delete_post/<str:id>/', views.delete_post, name='delete_post'),
]
