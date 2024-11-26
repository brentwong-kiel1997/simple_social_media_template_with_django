from django.urls import path
from . import views

urlpatterns = [
    path('', views.events, name='events'),
    path('event/<str:event_id>/', views.single_event, name='single_event'),
    path('event_post/<str:even_post_id>/', views.event_post, name='event_post'),
    path('delete_event/<str:event_id>/', views.delete_event, name='delete_event'),
    path('delete_event_post/<str:even_post_id>/', views.delete_event_post, name='delete_event_post'),
    path('add_event', views.add_event, name='add_event'),
    path('edit_event/<str:event_id>/', views.edit_event, name='edit_event'),
    path('add_event_post/<str:event_id>/', views.create_event_post, name='add_event_post'),
    path('edit_event_post/<str:post_id>/', views.edit_event_post, name='edit_event_post'),
]