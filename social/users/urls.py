# users/urls.py
from django.urls import path
from . import views
from django.contrib.auth.views import LogoutView


urlpatterns = [
    path('register/', views.register_user, name='register'),
    path('login/', views.login_user, name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('profile/', views.profile, name='profile'),
    path('edit_profile', views.edit_profile, name='edit_profile'),
    path('delete_profile', views.delete_profile, name='delete_profile'),
    path('users', views.users, name='users'),
    path('users/<str:user_id>', views.user_info, name='user_info'),
    path('message/<str:recipient_id>', views.message, name='message'),
    path('message_list', views.message_list, name='message_list'),
]