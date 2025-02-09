from . import views
from django.urls import path
from .views import newsletter_subscription, contact, welcome

urlpatterns = [
    path('', welcome, name='welcome'),  # For the welcome page
    path('home/', views.PostList.as_view(), name='home'),  # For the blog home page
    path('contact/', contact, name='contact_form'),
    path('subscribe/', newsletter_subscription, name='newsletter_subscription'),
    path('like/<slug:slug>/', views.PostLike.as_view(), name='post_like'),
    path('<slug:slug>/', views.PostDetail.as_view(), name='post_detail'),
]