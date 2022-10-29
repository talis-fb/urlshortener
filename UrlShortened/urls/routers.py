from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="home"),
    path('add', views.add_url, name="add"),
    path('register', views.add_url, name="register"),
    path('<str:hash>', views.get_url, name="main"),
]
