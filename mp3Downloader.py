import yt_dlp

playlist_url = (
    "https://www.youtube.com/playlist?list=PLrObs0z85ESLbuePI5wZyWGyJTmpGxpR7"
)

ydl_opts = {
    "extract_audio": True,
    "format": "bestaudio",
    "outtmpl": "./downloads/%(title)s.%(ext)s",
    "postprocessors": [
        {
            "key": "FFmpegExtractAudio",
            "preferredcodec": "mp3",
            "preferredquality": "192",
        }
    ],
    "ignoreerrors": True,
    # "lazy_playlist": True,
    "playliststart": 131,
}

videos_in_playlist = yt_dlp.YoutubeDL(ydl_opts).extract_info(
    playlist_url, download=False, process=False
)


count = 0
flag = False
for video in videos_in_playlist["entries"]:
    count += 1
    title = video["title"]
    print(f"{count} Title: {title}")

    if not flag:
        option = input(
            "Do you want to download this audio? (y/n): \n q to quit\n d to download all\n"
        )
        if option == "y":
            yt_dlp.YoutubeDL(ydl_opts).download([video["url"]])
        elif option == "q":
            break
        elif option == "d":
            yt_dlp.YoutubeDL(ydl_opts).download([video["url"]])
            flag = True
        else:
            print("Skipped")
    else:
        yt_dlp.YoutubeDL(ydl_opts).download([video["url"]])
