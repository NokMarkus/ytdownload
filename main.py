import yt_dlp
import os

def progressfunc(d):
    if d['status'] == 'downloading':
        print(f"\\downlaod in progress. {d['_percent_str']} @ {d['_speed_str']} | ETA: {d['eta']}s", end="")
    elif d['status'] == 'finished':
        print("\ndownloading complete")

def useroptions(typeofdownload, output_dir):
    options = {
        'progress_hooks': [progressfunc],
        'outtmpl': os.path.join(output_dir, '%(title)s.%(ext)s'),
    }

    if typeofdownload == "1":
        options['format'] = 'best'
    elif typeofdownload == "2":
        options['format'] = 'bestaudio/best'
        options['postprocessors'] = [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }]
    elif typeofdownload == "3":
        options['noplaylist'] = False
        options['format'] = 'best'
    else:
        raise ValueError("out of range download.")

    return options

def actualDownloadFunc():
    url = input("link to a video or playlist in YouTube: ").strip()
    download_type = input("download, (1) video, (2) audio only, or (3) a playlist? (Choose: 1, 2 or 3): ").strip()

    output_dir = 'downloaded'
    os.makedirs(output_dir, exist_ok=True)

    try:
        options = useroptions(download_type, output_dir)
        print("\nfetching info..")
        with yt_dlp.YoutubeDL(options) as ydl:
            ydl.download([url])
    except ValueError as e:
        print(f"error: {e}")
    except Exception as e:
        print(f"error occured: {e}")

if __name__ == "__main__":
    actualDownloadFunc()
