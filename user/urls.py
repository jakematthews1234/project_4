from django.urls import path
from django.contrib.auth import views as authorisation_views
from . import views


urlpatterns = [
    path('login/', authorisation_views.LoginView.as_view(template_name='user/login.html'), name='login_user'),
    path('register/', views.register, name='register_user'),
    path('logout/', authorisation_views.LogoutView.as_view(template_name='user/logout.html'), name='logout_user'),
]