
from django.urls import path
from django.contrib.auth import views as auth_views
from .views import register_user, user_profile


app_name = 'users'


urlpatterns = [
    path('register/', register_user, name='register_user'),
    path('login/', auth_views.LoginView.as_view(template_name='users/login.html'), name='login_user'),
    path('logout/', auth_views.LogoutView.as_view(template_name='users/logout.html'), name='logout_user'),
    path('profile/', user_profile, name='user_profile'),


]
