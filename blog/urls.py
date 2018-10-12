
from django.urls import path
from .views import PostCreateView, PostListView, PostDetailView, PostUpdateView, PostDeleteView, UserPostListView, about_page


app_name = 'blog'


urlpatterns = [
    path('home', PostListView.as_view(), name='blog_home_page'),
    path('user/<str:username>/', UserPostListView.as_view(), name='blog_user_posts'),
    path('create', PostCreateView.as_view(), name='blog_create_page'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='blog_detail_page'),
    path('update/<int:pk>/', PostUpdateView.as_view(), name='blog_update_page'),
    path('delete/<int:pk>/', PostDeleteView.as_view(), name='blog_delete_page'),
    path('about', about_page, name='blog_about_page'),
]
