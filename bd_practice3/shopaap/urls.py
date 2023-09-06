from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('shop', views.shop),
    path('group', views.group_list),
    path('products', views.product_list),
]
