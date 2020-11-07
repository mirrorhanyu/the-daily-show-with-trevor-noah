import youtube_dl

from youtube.youtube import fetch_youtube_feed_entries

entries = fetch_youtube_feed_entries()

with youtube_dl.YoutubeDL({
    'outtmpl': 'youtube-download-file',
    'writesubtitles': True,
    'subtitlesformat': 'srt/ass/vtt/best',
    'subtitle': '--write-sub --sub-lang en',
}) as ydl:
    ydl.download([f'https://www.youtube.com/watch?v={entries[2].video_id}'])