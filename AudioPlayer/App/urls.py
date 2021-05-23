from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include
from . import views

app_name = "App"

urlpatterns = [
    path("home/", views.index, name="index"),
    path("songs/", views.song_list, name="song_list"),
]
