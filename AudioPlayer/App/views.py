# Create your views here.
from django.shortcuts import render, redirect

# imported our models
from django.core.paginator import Paginator
from App.models import Song


def index(request):
    paginator = Paginator(Song.objects.all(), 1)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {"page_obj": page_obj}
    return render(request, "App/index.html", context)


def song_list(request):
    queryset = Song.objects.all()
    context = {"object_list": queryset}
    return render(request, "App/song_list.html", context)
