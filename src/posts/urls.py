from django.contrib import admin
from django.urls import path
from posts.views import post_create, post_detail, post_list, post_update, post_delete

app_name="posts"

urlpatterns = [
    path('', post_list, name='list'),
    path('create/',  post_create),
    # path('<int:id>/',  post_detail, name='detail'),
    path('<slug>/',  post_detail, name='detail'),
    path('<slug>/edit/', post_update, name='update'),
    path('<slug>/delete/', post_delete),
]
