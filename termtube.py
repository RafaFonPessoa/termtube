import argparse
import os
from termtube_video import download_video
from termtube_audio import download_audio

def main():
    parser = argparse.ArgumentParser(description="Download videos and audios from Youtube!")
    parser.add_argument("url", help="URL do vídeo a ser baixado.")
    parser.add_argument("-f", "--formato", help="Formatos disponíveis: mp4, webm, mkv, flv, avi and mov.")
    parser.add_argument("-p", "--path", help="Folder path ex: ~/Downloads/")
    parser.add_argument("-a", "--audio", action="store_true", help="Baixar apenas o áudio.") # Correção: adicionado action="store_true"
    args = parser.parse_args()

    if args.audio:
        download_audio(args.url, args.path)
    else:
        download_video(args.url, args.path, args.formato)

    if args.path:
        print(f"Arquivo baixado para a pasta: {args.path}")
    else:
        print("Arquivo baixado para a pasta Downloads!")

if __name__ == '__main__':
    main()
