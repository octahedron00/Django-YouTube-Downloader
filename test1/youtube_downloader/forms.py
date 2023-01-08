import pytube.exceptions
from django import forms
from django.core.exceptions import ValidationError
from pytube import YouTube, Playlist


class DownloadVideoForm(forms.Form):
    text_link = forms.CharField(max_length=500)

    CHOICES_is_1080 = [
        ('false', 'Best Resolution Only'),
        ('true', 'FHD(1920*1080) Preferred')
    ]
    radio_is_1080 = forms.ChoiceField(
        widget=forms.RadioSelect,
        choices=CHOICES_is_1080,
        initial='false'
    )

    CHOICES_add_channel = [
        ('true', 'With Channel Name'),
        ('false', 'Without Channel Name')
    ]
    radio_add_channel = forms.ChoiceField(
        widget=forms.RadioSelect,
        choices=CHOICES_add_channel,
        initial='true'
    )

    def clean_link(self):
        link = self.cleaned_data['text_link']
        try:
            _ = YouTube(link)
        except pytube.exceptions.RegexMatchError:
            print(link, 'return 2')
            return 2
        except pytube.exceptions.VideoPrivate or pytube.exceptions.VideoUnavailable or pytube.exceptions.VideoRegionBlocked or pytube.exceptions.HTMLParseError:
            print(link, 'return 1')
            return 1

        return 0

    def clean_link_list(self):
        link = self.cleaned_data['text_link']
        try:
            _ = Playlist(link)
        except:
            return 1

        return 0


class DownloadAudioForm(forms.Form):
    text_link = forms.CharField(max_length=500)

    CHOICES_encoding_to_mp3 = [
        ('false', 'Opus file with name of MP3, 160kbps(Faster Download)'),
        ('true', 'MP3 file, converted from Opus, 320kbps size, same sound(Slower Download)'),
    ]
    radio_encoding_to_mp3 = forms.ChoiceField(
        widget=forms.RadioSelect,
        choices=CHOICES_encoding_to_mp3,
        initial='false'
    )

    CHOICES_add_channel = [
        ('true', 'With Channel Name'),
        ('false', 'Without Channel Name')
    ]
    radio_add_channel = forms.ChoiceField(
        widget=forms.RadioSelect,
        choices=CHOICES_add_channel,
        initial='true'
    )

    def clean_link(self):
        link = self.cleaned_data['text_link']
        try:
            _ = YouTube(link)
        except pytube.exceptions.RegexMatchError:
            print(link, 'return 2')
            return 2
        except pytube.exceptions.VideoPrivate or pytube.exceptions.VideoUnavailable or pytube.exceptions.VideoRegionBlocked or pytube.exceptions.HTMLParseError:
            print(link, 'return 1')
            return 1

        return 0

    def clean_link_list(self):
        link = self.cleaned_data['text_link']
        try:
            _ = Playlist(link)
        except:
            return 1

        return 0
