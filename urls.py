from django.urls import path 
from . import views

app_name = "flights"

urlpatterns = [
    path('', views.index, name="index"),
    path('<str:flight>', views.flight, name="flight")
] 