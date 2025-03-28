import os
import yt_dlp

def download_audio(url, path_directory=None):
    yt_opts = {
        'format': 'bestaudio/best',
        'postprocessors': [{  # Conversão obrigatória para MP3
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'mp3',
        'preferredquality': '192',
    }],
        'outtmpl': os.path.join(path_directory or os.path.expanduser('~/Downloads/'), '%(title)s.%(ext)s'),
        'ffmpeg_location': '/usr/bin/ffmpeg',
        'keepvideo': False  # Remove o arquivo de vídeo após a conversão
    }

    with yt_dlp.YoutubeDL(yt_opts) as ydl:
        ydl.download([url])
