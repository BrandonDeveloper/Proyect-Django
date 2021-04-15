"""Estamos en el modulo URL"""
from django.urls import path
from django.http import HttpResponse
from platzigram import views as local_views
from posts import views as posts_views


urlpatterns = [
    path("hello-world/",local_views.hello_world),
    path("num/",local_views.sorted),
    path("hi/<str:name>/<int:age>/",local_views.say_hi),

    path("posts/",posts_views.list_posts),
]
