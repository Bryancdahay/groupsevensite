from django.urls import path, include
from . import views
from . views import AuthView, home
from django.contrib.auth import views as auth_views
from django.contrib import admin
from django.contrib.auth.views import LoginView



urlpatterns = [
    path("", views.home, name="home"),
    path("signup/", AuthView, name="signup"),   

    path('login/', auth_views.LoginView.as_view(template_name='registration/login.html'), name='login'),

    path('admin/', admin.site.urls),
    path("logout/", auth_views.LogoutView.as_view(next_page='login'), name="logout"),
    path("accounts/", include("django.contrib.auth.urls")),
    path('gender/list', views.gender_list),
    path('gender/add', views.add_gender),
    path('gender/edit/<int:genderId>', views.edit_gender),
    path('gender/delete/<int:genderId>', views.delete_gender),
    path('user/list', views.user_list),
    path('user/add', views.add_user),
]

