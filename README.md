# Django-YouTube-Downloader

YouTube &amp; Playlist Downloading Webpage Source Code, Based on Django, FFmpeg and pytube.

# Metadata of the Django Project

## project name

**test1** (it was just for test, and now I can't change this..)

## app name

**index** (for index page)

**youtube-downloader** (for YouTube Downloader page)

*new* (not used, it was just for test)

## folder

**static** (just for style.css here)

**template** (for the html files, js script is included in html)

## used package

**Django** (for backend)

**pytube** (for download youtube)

**cryptography** (for symmetric encrypting of file address at GET of download/delete link)

# simple stream of each app

## index

Providing a link to the downloader page, not necessary.

## youtube_downloader

**Main Page(/)** : Providing links to 4 downloading options. (Video/Audio), (One link/Playlist)

**Download a Video(/dv/)** : receiving about the link and the settings.

> Download pages, after receiving the link and settings, self-check whether the link is valid or not, 
> 
> and if the link is not valid, they simply show error messages.
> 
> If the link is valid -> **they show new pages(without any change of link)**, which **automatically open pages to download a video**, 
>
> and **to delete that video from the server-side(to save the storage capacity).**

**Download Videos from a Playlist(/dvl/)** : works same, but for a playlist.

**Download an Audio(/da/)** : works same, but it downloads only an audio.

**Download Audios from a Playlist(/dal/)** : works same, but for a playlist, and only audios.

**YouTube downloading code is same as [This Code](https://www.github.com/octahedron00/YouTube-Playlist-Downloader)**
