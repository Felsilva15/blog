from django.urls import path
from .views import PostListView, PostDetailView
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', PostListView.as_view(), name='post-list'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('about/', views.about, name='about'),
    path('login/', auth_views.LoginView.as_view(template_name='blog/login.html'), name='login'),
    # Add more URLs as needed
]
