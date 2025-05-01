from .import views
from django.urls import path

urlpatterns = [
    path('', views.make_instance,name =('make_instance')),
    path('<uuid:chat_id>',views.home,name='home'),
    path("<uuid:chat_id>/a", views.get_answer,name='get_answer'),
    path('<uuid:chat_id>/c',views.clear,name='clear'),
]
