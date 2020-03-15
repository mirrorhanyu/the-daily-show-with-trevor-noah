import glob

import requests
from you_get.extractors import youtube

from file_utils import create_google_secret_account_credential
from google_drive import upload
from datetime import datetime, timezone, timedelta

from notify import send_email
from youtube_feed import YoutubeFeed

create_google_secret_account_credential()

youtube_feeds_url = 'https://www.youtube.com/feeds/videos.xml?channel_id=UCwWhs_6x42TyRM4Wstoq8HA'
feeds_xml = requests.get(youtube_feeds_url).text
entries = YoutubeFeed(feeds_xml).entries

for entry in entries:
    if datetime.fromisoformat(entry.published) + timedelta(hours=4) >= datetime.now(timezone.utc):
        youtube.download(url=f'https://www.youtube.com/watch?v={entry.videoId}', output_dir='.', merge=True)
        folder_id = '1vAn92qcBDwaZLc7dbqqdaqwSbszJw1cw'
        [upload(file_name, folder_id) for file_name in glob.glob(f'{entry.title.split(" | ")[0][:80]}*.*')]
        send_email(from_address='hanhaneita@gmail.com',
                   to_address='mirrorhanyu@gmail.com',
                   subject=f'[Youtube Download] - {entry.title}',
                   text='Done!')
