from django.contrib import admin
from django.urls import path
from django.contrib.auth import views as auth_views
from blog import views as blog_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('register/', blog_views.register, name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='blog/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='blog/logout.html'), name='logout'),
    path('', blog_views.PostListView.as_view(), name='post-list'),
    path('post/<int:pk>/', blog_views.PostDetailView.as_view(), name='post-detail'),
    path('about/', blog_views.about, name='about'),
]
