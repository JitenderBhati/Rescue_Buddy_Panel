from django.urls import path
from . import views

urlpatterns = [
    path('', views.login, name="Admin Login"),
    path('add_item/', views.add_item, name ="Add Items"),
    path('logout/', views.logout, name="Log Out")
]
