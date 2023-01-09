from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return render(request, "index/load_to_youtube_downloader.html")
