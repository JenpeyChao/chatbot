from .import views
from django.urls import path

urlpatterns = [
    path('', views.home,name =('home')),
    path("a", views.get_answer,name='get_answer'),
]
