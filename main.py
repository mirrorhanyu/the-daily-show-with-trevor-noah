from time import sleep

from bilibili.bilibili import upload_files_to_bilibili
from google.google import send_notify_email
from utils.file_utils import remove_folder
from video.video import generate_video_with_subtitle
from youtube.youtube import fetch_youtube_feed_entries, download

ENOUGH_HOURS_TO_WAIT_FOR_YOUTUBE_SUBTITLE = 6

latest_youtube_entries = [entry for entry in fetch_youtube_feed_entries()][:2]
for entry in reversed(latest_youtube_entries):
    download(entry.video_id)
    generate_video_with_subtitle()
    upload_files_to_bilibili(entry)
    send_notify_email(f'[Youtube Downloaded & Uploaded] - {entry.title}')
    # sleep 30 seconds to avoid bilibili upload issue
    sleep(30)
    remove_folder('download')
