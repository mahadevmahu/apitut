from django.urls import path
from . import views

urlpatterns = [
    path('',views.posts,name="posts"),
    path('view/<pk>',views.post,name="post"),
    path('create/',views.create_post,name="create_post"),
    path('edit/<pk>',views.edit_post,name="edit_post"),
]