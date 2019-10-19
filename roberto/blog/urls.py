from django.urls import path 
from . import views


urlpatterns = [
     path('blog/', views.blog, name="blog"),
     path('<int:id>/singleblog', views.singleblog, name="singleblog"),
]