from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('message/', views.message),
    path('chat_service/', views.chat_service),
]