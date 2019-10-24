from django.urls import path, include
from rober import views




urlpatterns = [
    path('', views.home, name="home"),
    path('about/', views.about, name="about"),
]

