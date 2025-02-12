from . import views
from django.urls import path
from .views import (
    newsletter_subscription,
    contact,
    welcome,
    post_update,  # Keep if this is a function-based view
    PostDetail,  # This is a class-based view
    PostLike,
    PostList,
    post_delete
)




urlpatterns = [
    path('', welcome, name='welcome'),  # For the welcome page
    path('home/', views.PostList.as_view(), name='home'),  # For the blog home page
    path('contact/', contact, name='contact_form'),
    path('subscribe/', newsletter_subscription, name='newsletter_subscription'),
    path('like/<slug:slug>/', views.PostLike.as_view(), name='post_like'),
    path('<slug:slug>/', views.PostDetail.as_view(), name='post_detail'),
    path('<slug:slug>/', post_detail.as_view(), name='post_detail'),  # View post
    path('post/edit/<slug:slug>/', post_update, name='post_update'),  # No `.as_view()
    path('post/delete/<slug:slug>/', post_delete, name='post_delete'),
    path('post/create/', views.post_create, name='post_create'), # Add Post
    path('<slug:slug>/edit_comment/<int:comment_id>',
         views.comment_edit, name='comment_edit'),
    path('<slug:slug>/delete_comment/<int:comment_id>',
         views.comment_delete, name='comment_delete'),

]