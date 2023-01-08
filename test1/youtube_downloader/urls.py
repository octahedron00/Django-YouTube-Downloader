from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

app_name = 'youtube_downloader'

urlpatterns = [
    path('', views.index, name='index'),
    path('dvl/', views.download_video_list, name='dvl'),
    path('dal/', views.download_audio_list, name='dal'),
    path('dv/', views.download_video, name='dv'),
    path('da/', views.download_audio, name='da'),
    path('download/<str:download_address>', views.serve_file, name='download'),
    path('delete/<str:download_address>', views.delete_file, name='delete')
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
