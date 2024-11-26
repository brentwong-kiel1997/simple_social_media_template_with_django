# users/urls.py
from tempfile import template

from django.urls import path
from . import views
from django.contrib.auth.views import LogoutView

from django.contrib.auth import views as auth

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
    path('comment_list', views.comment_list, name='comment_list')
]

urlpatterns += [path('reset_password/', auth.PasswordResetView.as_view(template_name='users/reset_password.html'),
                     name="reset_password"),
                path('reset_password_sent/',
                     auth.PasswordResetDoneView.as_view(template_name='users/reset_password_sent.html'),
                     name="password_reset_done"),
                path('reset/<uidb64>/<token>/',
                     auth.PasswordResetConfirmView.as_view(template_name='users/reset_password_form.html'),
                     name="password_reset_confirm"),
                path('reset_password_complete/',
                     auth.PasswordResetCompleteView.as_view(template_name='users/reset_password_complete.html'),
                     name="password_reset_complete"), ]
