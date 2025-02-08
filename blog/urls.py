from . import views
from django.urls import path
from .views import newsletter_subscription
from .views import contact



urlpatterns = [
    path('', views.PostList.as_view(), name='home'),
    path('<slug:slug>/', views.PostDetail.as_view(), name='post_detail'),
    path('like/<slug:slug>', views.PostLike.as_view(), name='post_like'),
    path('subscribe/', newsletter_subscription, name='newsletter_subscription'),
    path('contact/', contact, name='contact_form'),
]

