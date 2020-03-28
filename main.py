import glob
from time import sleep

# from bilibili.bilibili import upload_files_to_bilibili
# from google.google import send_notify_email, upload_files_to_drive_by
# from utils.file_utils import remove_folder
from typing import Callable, Any

from moviepy.video.VideoClip import TextClip
from moviepy.video.compositing.CompositeVideoClip import CompositeVideoClip
from moviepy.video.io.VideoFileClip import VideoFileClip
from moviepy.video.tools.subtitles import SubtitlesClip

from utils.file_utils import is_video, is_subtitle, add_prefix_to_filename
from utils.time_utils import is_within_hours
# from video.video import generate_video_with_subtitle
from youtube.youtube import fetch_youtube_feed_entries, download

for entry in fetch_youtube_feed_entries():
    if is_within_hours(entry.published, hours=8):
        download(entry.video_id)
        # generate_video_with_subtitle()
        # upload_files_to_drive_by(entry)
        # upload_files_to_bilibili(entry)
        # send_notify_email(f'[Youtube Downloaded & Uploaded] - {entry.title}')
        # sleep 30 seconds to avoid bilibili upload issue
        # sleep(30)
        # remove_folder('download')
        video_path = next(path for path in glob.glob('download/*') if is_video(path))
        subtitle_path = next(path for path in glob.glob('download/*') if is_subtitle(path))
        generator: Callable[[Any], TextClip] = lambda txt: TextClip(txt,
                                                                    font='./video/GothamMedium.ttf',
                                                                    fontsize=35, color='white',
                                                                    bg_color='#00000066')
        subtitle = SubtitlesClip(subtitle_path, generator).set_position(('center', 'bottom'))
        video = VideoFileClip(video_path, audio=True)
        composed_video = CompositeVideoClip([video, subtitle])
        composed_video.write_videofile(add_prefix_to_filename(video_path, '[WITH-SUBTITLE] '),
                                       threads=4,
                                       fps=video.fps,
                                       temp_audiofile="temp-audio.m4a",
                                       remove_temp=True,
                                       audio_codec="aac")
