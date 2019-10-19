from django.urls import path, include
from rober import views




urlpatterns = [
    path('', views.home, name="home"),
    path('about/', views.about, name="about"),
    path('contact/', views.contact, name="contact"),
    path('room/', views.room, name="room"),
    path('singleroom/', views.singleroom, name="singleroom"),
]

