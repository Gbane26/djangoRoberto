from django.urls import path, include
from . import views




urlpatterns = [
    path('', views.room, name="room"),
    path('singleroom/', views.singleroom, name="singleroom"),
]

