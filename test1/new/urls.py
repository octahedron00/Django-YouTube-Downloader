from django.urls import path

from . import views

app_name = 'new'

urlpatterns = [
    path('', views.index, name='redirection_to_youtube_downloader')
]