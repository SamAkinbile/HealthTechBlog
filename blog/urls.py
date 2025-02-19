from django.urls import path
from . import views  # Keep this if you are using views.something

from .views import (
    newsletter_subscription, contact, welcome, post_update, PostDetail,
    PostLike, PostList, post_delete
)

urlpatterns = [
    path('', welcome, name='welcome'),
    path('home/', PostList.as_view(), name='home'),
    path('contact/', contact, name='contact_form'),
    path('subscribe/', newsletter_subscription, 
         name='newsletter_subscription'),
    path('like/<slug:slug>/', PostLike.as_view(), name='post_like'),
    path('<slug:slug>/', PostDetail.as_view(), name='post_detail'),
    path('post/edit/<slug:slug>/', post_update, name='post_update'),
    path('post/delete/<slug:slug>/', post_delete, name='post_delete'),
    path('post/create/', views.post_create, name='post_create'),
    path(
        '<slug:slug>/edit_comment/<int:comment_id>/',
        views.comment_edit,
        name='comment_edit',
    ),
    path(
        '<slug:slug>/delete_comment/<int:comment_id>/',
        views.comment_delete,
        name='comment_delete',
    ),
]

# Ensure the file ends with a newline
