from django.urls import path
from . import views


urlpatterns = [
    path('hello/', views.hello_request, name="hello_request"),
    path('form/', views.formstest, name="forms_test"),
    path('upload', views.upload_tes, name="upload"),
]
