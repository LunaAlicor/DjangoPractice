from django.urls import path
from . import views

urlpatterns = [
    path('', views.IndexView.as_view(), name="index"),
    path('shop', views.shop, name="shop"),
    path('group', views.group_list, name="group-list"),
    path('products', views.ProductListView.as_view(), name="products"),
    path('orders', views.order_list, name="orders"),
    path("create_product", views.ProductCreateView.as_view(), name='create_product'),
    path("create_order", views.create_order, name='create_order'),
    path("products/<int:pk>/", views.ProductDitailsView.as_view(), name="product_detail"),
    path('products/<int:pk>/update', views.ProductUpdateView.as_view(), name="update_product"),
    path('products/<int:pk>/delete', views.ProductDeleteView.as_view(), name="delete_product"),
]
