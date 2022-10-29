from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="home"),
    path('add', views.add_url, name="add"),
    path('<str:hash>', views.get_url, name="main"),
]
