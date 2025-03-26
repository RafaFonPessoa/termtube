import yt_dlp 
import os
import sys

def download_video(url, path_directory):
    ydl_opts = {
                'outtmpl': os.path.join(path_directory, '%(title)s.%(ext)s'),
                'format': 'bestvideo[ext=mp4]+bestaudio[ext=m4a]/best[ext=mp4]/best',
            }
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])


def main():
    if len(sys.argv) < 2:
        print("Uso: termtube <URL_do_video>")
        sys.exit(1)

    url_video = sys.argv[1]
    path_directory = os.path.expanduser('~/Downloads')
    download_video(url_video, path_directory)
    print(f"Video baixado para: {path_directory}")


if __name__ == '__main__':
    main()


