import requests

from youtube.youtube_feed import YoutubeFeed


def fetch_youtube_feed_entries():
    youtube_feeds_url = 'https://www.youtube.com/feeds/videos.xml?channel_id=UCwWhs_6x42TyRM4Wstoq8HA'
    feeds_xml = requests.get(youtube_feeds_url).text
    return YoutubeFeed(feeds_xml).entries
