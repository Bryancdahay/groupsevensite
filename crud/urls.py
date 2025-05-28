from django.urls import path, include
from . import views
from . views import AuthView
from django.contrib.auth import views as auth_views
from django.contrib import admin




urlpatterns = [
    path("", views.home, name="base"),
    path("signup/", AuthView, name="signup"),   
    path('login/', auth_views.LoginView.as_view(template_name='registration/login.html'), name='login'),
    path("logout/", auth_views.LogoutView.as_view(next_page='login'), name="logout"),
    path("accounts/", include("django.contrib.auth.urls")),
    path('gender/list', views.gender_list),
    path('gender/add', views.add_gender),
    path('gender/edit/<int:genderId>', views.edit_gender),
    path('gender/delete/<int:genderId>', views.delete_gender),
    path('user/list', views.user_list),
    path('user/add', views.add_user),
]

