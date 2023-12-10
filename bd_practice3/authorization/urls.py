from django.contrib import admin
from django.urls import path, include
from . import views
from django.contrib.auth.views import LoginView


urlpatterns = [
    # path('', views.my_login, name='login'),
    path('login/',
         views.LoginView.as_view(template_name='authorization/login.html',
                                 redirect_authenticated_user=True),
         name='login'),
    path('cookie/set/', views.set_cookie, name='set_cookie'),
    path('cookie/get/', views.get_cookie_view, name='get_cookie',),
    path('session/set/', views.set_session_view, name='set_session'),
    path('session/get/', views.get_session_view, name='get_session'),
    # path('logout', views.logout_view, name='logout'),
    path('logout', views.MyLogoutView.as_view(), name='logout'),

]
