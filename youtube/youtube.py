import requests
from you_get.extractors import youtube

from youtube.youtube_feed import YoutubeFeed


def fetch_youtube_feed_entries():
    youtube_feeds_url = 'https://www.youtube.com/feeds/videos.xml?user=TEDEducation'
    feeds_xml = requests.get(youtube_feeds_url).text
    return YoutubeFeed(feeds_xml).entries


def download(video_id):
    youtube.download(url=f'https://www.youtube.com/watch?v={video_id}', output_dir='download', merge=True, caption=True)
