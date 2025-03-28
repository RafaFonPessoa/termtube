import os
import yt_dlp 

def download_video(url, path_directory=None, video_format=None):
    ydl_opts = {}
    
    if path_directory:
        ydl_opts['outtmpl'] = os.path.join(path_directory, '%(title)s.%(ext)s')
    else:
        ydl_opts['outtmpl'] = os.path.join('~/Downloads/', '%(title)s.%(ext)s')


    if video_format:
        ydl_opts['format'] = video_format
    else:
        ydl_opts['format'] = 'bestvideo[ext=mp4]+bestaudio[ext=mp3]/best[ext=mp4]/best'
    

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])
