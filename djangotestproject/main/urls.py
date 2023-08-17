from django.urls import path
from . import views

urlpatterns = [
    path('', views.idex),
    path('about', views.about),
]
