import os
import datetime
import subprocess
from pytube import Playlist, YouTube

# download_path here.
download_path = "C:\\Python\\youtube\\download"


def get_video(link: str, is_1080: bool = False, add_channel: bool = True):
    # Downloading
    # use_oauth : for download YouTube_Music-only, if you have YouTube Music account.
    yt = YouTube(link, use_oauth=True)

    timestamp = str(datetime.datetime.now())[-6:]

    # to see what filter has the best quality : here
    print("Filters :", len(yt.streams.filter(only_video=True)), yt.streams.filter(only_video=True))

    # the best quality : ~160kbps of webm, or the best of existing filters.
    video = yt.streams.filter(only_video=True).get_by_itag('137')
    if video is None:
        video = yt.streams.filter(only_video=True).get_by_itag('248')
    if not is_1080 or video is None:
        video = yt.streams.filter(only_video=True).order_by("resolution")[-1]

    audio = yt.streams.filter(only_audio=True).order_by("abr")[-1]

    out_audio = audio.download(output_path=download_path)
    base, _ = os.path.splitext(out_audio)
    filename = str(base).replace(download_path + '\\', "")

    filename = filename + "_" + timestamp

    if add_channel:
        forbidden_chars = '*\\/|?:<>'
        author = ''.join([x if x not in forbidden_chars else ' ' for x in yt.author])
        filename = author + " - " + filename

    filename = download_path + '\\' + filename
    os.rename(out_audio, filename + "_.mp3")

    # download to the path, you can change this.
    out_video = video.download(output_path=download_path)
    base, _ = os.path.splitext(out_video)
    os.rename(out_video, filename + "_.mp4")

    print(subprocess.run(f'ffmpeg -i "{filename}_.mp4" -i "{filename}_.mp3" -c:v copy -c:a aac '
                         f'"{filename}.mp4"',
                         shell=True, capture_output=True).stdout)
    os.remove(filename + "_.mp3")
    os.remove(filename + "_.mp4")
    return f'{filename}.mp4'


def get_video_list(link_list: str, is_1080: bool = False, add_channel: bool = True):
    p = Playlist(link_list)
    files = []

    for link in p.video_urls:
        files.append(get_video(link=link, is_1080=is_1080, add_channel=add_channel))

    return files


def get_audio(link: str, encoding_to_mp3: bool = False, add_channel: bool = True):
    yt = YouTube(link)

    timestamp = str(datetime.datetime.now())[-6:]

    audio = yt.streams.filter(only_audio=True).order_by("abr")[-1]

    out_audio = audio.download(output_path=download_path)
    base, _ = os.path.splitext(out_audio)
    filename = str(base).replace(download_path + '\\', "")

    filename = filename + "_" + timestamp

    if add_channel:
        forbidden_chars = '*\\/|?:<>'
        author = ''.join([x if x not in forbidden_chars else '_' for x in yt.author])
        filename = author + " - " + filename

    filename = download_path + '\\' + filename
    os.rename(out_audio, filename + "_.webm")

    if encoding_to_mp3:
        print(subprocess.run(f'ffmpeg -i "{filename}_.webm" -codec:a libmp3lame -b:a 320k "{filename}.mp3"',
                             shell=True, capture_output=True).stdout)
        os.remove(filename + "_.webm")
    else:
        os.rename(filename + "_.webm", filename + ".mp3")
    return f'{filename}.mp3'


def get_audio_list(link_list: str, encoding_to_mp3: bool = False, add_channel: bool = True):
    p = Playlist(link_list)
    files = []

    for link in p.video_urls:
        files.append(get_audio(link=link, encoding_to_mp3=encoding_to_mp3, add_channel=add_channel))

    return files


if __name__ == "__main__":
    print(get_video(input("Download Video - Link:"), add_channel=True))
    print(get_audio(input("Download Audio - Link:"), add_channel=True))
    print(get_video_list(input("Download Video List - Link:"), add_channel=True, is_1080=False))
    print(get_audio_list(input("Download Audio List - Link:"), add_channel=True))
