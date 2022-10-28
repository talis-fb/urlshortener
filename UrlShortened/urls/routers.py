from django.urls import path
from . import views

urlpatterns = [
    path('add', views.add_url, name="Home"),
    path('<str:hash>', views.get_url, name="Main"),
]
