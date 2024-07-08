# blog/urls.py
from django.urls import path
from .views import PostListView, PostDetailView
from django.urls import path
from . import views

urlpatterns = [
    path('', PostListView.as_view(), name='post-list'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('about/', views.about, name='about'),
    # Add more URLs as needed
]
