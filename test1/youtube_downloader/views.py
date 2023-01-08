import os
import json

from django.shortcuts import render
from django.http import HttpResponse, HttpRequest, HttpResponseRedirect, FileResponse
from django.template import loader, RequestContext
from django.urls import reverse
from django.core.files.base import ContentFile
from mimetypes import MimeTypes
from urllib.request import pathname2url
from cryptography.fernet import Fernet

from .forms import DownloadVideoForm, DownloadAudioForm
from .download import *

# Create your views here.

KEY = b'4_zFSbQ8iN5fQ-yPq8zjWIpG2ZZtgXmsE-EltYnuQX8='


def serve_file(request, download_address: str):
    f = Fernet(KEY)
    file_address = str(f.decrypt(bytes(download_address, encoding='utf-8')).decode('utf-8'))

    print("SERVE:", file_address)

    length = os.path.getsize(file_address)
    content_type, _ = MimeTypes().guess_type(pathname2url(file_address))
    name = file_address.replace(download_path + '\\', "")

    response = FileResponse(open(file_address, 'rb'), as_attachment=True, filename=name)
    return response


def delete_file(request, download_address: str):
    f = Fernet(KEY)
    file_address = str(f.decrypt(bytes(download_address, encoding='utf-8')).decode('utf-8'))

    print("DELETE:", file_address)

    os.remove(file_address)
    return render(request, 'youtube_downloader/null.html')


def index(request: HttpRequest):
    return render(request, 'youtube_downloader/index.html')


def download_video_list(request: HttpRequest):
    print(request.method)
    if request.method == 'POST':
        print(request.POST)
        form = DownloadVideoForm(request.POST)
        print(request.POST['radio_add_channel'])
        context = {
            'form': form
        }

        if form.is_valid():
            if form.clean_link_list() == 0:
                is_1080 = False
                add_channel = True
                if request.POST['radio_is_1080'] == 'true':
                    is_1080 = True
                if request.POST['radio_add_channel'] == 'false':
                    add_channel = False
                print('DEBUG:', form.cleaned_data['text_link'])

                file_address_list = get_video_list(link_list=str(form.cleaned_data['text_link']), is_1080=is_1080, add_channel=add_channel)

                f = Fernet(KEY)

                download_address = [f.encrypt(bytes(file_address, encoding='utf-8')).decode('utf-8') for file_address in file_address_list]
                print(download_address)
                context = {
                    'file_addresses': download_address,
                    'file_addresses_json': json.dumps(download_address)
                }
                return render(request, 'youtube_downloader/complete.html', context)

            else:
                context['error'] = "Insert Correct YouTube Link"

    else:
        context = {
            'form': DownloadVideoForm()
        }
    return render(request, 'youtube_downloader/dvl.html', context)


def download_video(request: HttpRequest):
    print(request.method)
    if request.method == 'POST':
        print(request.POST)
        form = DownloadVideoForm(request.POST)
        print(request.POST['radio_add_channel'])
        context = {
            'form': form
        }

        if form.is_valid():
            if form.clean_link() == 0:
                is_1080 = False
                add_channel = True
                if request.POST['radio_is_1080'] == 'true':
                    is_1080 = True
                if request.POST['radio_add_channel'] == 'false':
                    add_channel = False
                print('DEBUG:', form.cleaned_data['text_link'])

                file_address = get_video(link=str(form.cleaned_data['text_link']), is_1080=is_1080, add_channel=add_channel)

                f = Fernet(KEY)

                download_address = [f.encrypt(bytes(file_address, encoding='utf-8')).decode('utf-8')]
                print(download_address)
                context = {
                    'file_addresses': download_address,
                    'file_addresses_json': json.dumps(download_address)
                }
                return render(request, 'youtube_downloader/complete.html', context)

            elif form.clean_link() == 2:
                context['error'] = "Insert Correct YouTube Link"
            elif form.clean_link() == 1:
                context['error'] = "Link is not valid : Can't Open"

    else:
        context = {
            'form': DownloadVideoForm()
        }
    return render(request, 'youtube_downloader/dv.html', context)


def download_audio_list(request: HttpRequest):
    print(request.method)
    if request.method == 'POST':
        print(request.POST)
        form = DownloadAudioForm(request.POST)
        print(request.POST['radio_add_channel'])
        context = {
            'form': form
        }

        if form.is_valid():
            if form.clean_link_list() == 0:
                encoding_to_mp3 = False
                add_channel = True
                if request.POST['radio_encoding_to_mp3'] == 'true':
                    encoding_to_mp3 = True
                if request.POST['radio_add_channel'] == 'false':
                    add_channel = False
                print('DEBUG:', form.cleaned_data['text_link'])

                file_address_list = get_audio_list(link_list=str(form.cleaned_data['text_link']),
                                                   encoding_to_mp3=encoding_to_mp3, add_channel=add_channel)

                f = Fernet(KEY)

                download_address = [f.encrypt(bytes(file_address, encoding='utf-8')).decode('utf-8') for file_address in
                                    file_address_list]
                print(download_address)
                context = {
                    'file_addresses': download_address,
                    'file_addresses_json': json.dumps(download_address)
                }
                return render(request, 'youtube_downloader/complete.html', context)

            else:
                context['error'] = "Insert Correct YouTube Link"

    else:
        context = {
            'form': DownloadAudioForm()
        }
    return render(request, 'youtube_downloader/dal.html', context)


def download_audio(request: HttpRequest):
    print(request.method)
    if request.method == 'POST':
        print(request.POST)
        form = DownloadAudioForm(request.POST)
        print(request.POST['radio_add_channel'])
        context = {
            'form': form
        }

        if form.is_valid():
            if form.clean_link() == 0:
                encoding_to_mp3 = False
                add_channel = True
                if request.POST['radio_encoding_to_mp3'] == 'true':
                    encoding_to_mp3 = True
                if request.POST['radio_add_channel'] == 'false':
                    add_channel = False
                print('DEBUG:', form.cleaned_data['text_link'])

                file_address = get_audio(link=str(form.cleaned_data['text_link']), encoding_to_mp3=encoding_to_mp3,
                                         add_channel=add_channel)

                f = Fernet(KEY)

                download_address = [f.encrypt(bytes(file_address, encoding='utf-8')).decode('utf-8')]
                print(download_address)
                context = {
                    'file_addresses': download_address,
                    'file_addresses_json': json.dumps(download_address)
                }
                return render(request, 'youtube_downloader/complete.html', context)

            elif form.clean_link() == 2:
                context['error'] = "Insert Correct YouTube Link"
            elif form.clean_link() == 1:
                context['error'] = "Link is not valid : Can't Open"

    else:
        context = {
            'form': DownloadAudioForm()
        }
    return render(request, 'youtube_downloader/da.html', context)
