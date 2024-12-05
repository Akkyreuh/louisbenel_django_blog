from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
    path('', views.list_posts, name='list_posts'),
    path('post/<int:id>/', views.post_detail, name='post_detail'),
    path('post/create/', views.create_post, name='create_post'),
    path('post/<int:id>/edit/', views.edit_post, name='edit_post'),
    path('post/<int:id>/add_comment/', views.add_comment, name='add_comment'),
    path('comment/<int:id>/edit/', views.edit_comment, name='edit_comment'),
    path('post/<int:id>/delete/', views.delete_post, name='delete_post'),
    path('comment/<int:id>/delete/', views.delete_comment, name='delete_comment'),
]
