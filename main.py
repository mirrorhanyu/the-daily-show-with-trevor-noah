import glob

import youtube_dl
from moviepy.video.VideoClip import TextClip
from moviepy.video.compositing.CompositeVideoClip import CompositeVideoClip
from moviepy.video.fx.margin import margin
from moviepy.video.io.VideoFileClip import VideoFileClip
from moviepy.video.tools.subtitles import SubtitlesClip

from env.bin.vtt_to_srt import vtt_to_srt
from utils.file_utils import is_vtt_subtitle
from youtube.youtube import fetch_youtube_feed_entries

entries = fetch_youtube_feed_entries()

with youtube_dl.YoutubeDL({
    'outtmpl': 'youtube-download-file',
    'writesubtitles': True,
    'subtitlesformat': 'srt',
    'subtitle': '--sub-lang en --write-sub --convert-subs srt',
}) as ydl:
    ydl.download([f'https://www.youtube.com/watch?v={entries[2].video_id}'])
    video_path = 'youtube-download-file'
    subtitle_path = next((path for path in glob.glob('youtube-download-file.en.*')), None)
    if is_vtt_subtitle(subtitle_path):
        vtt_to_srt(subtitle_path)
        subtitle_path = 'youtube-download-file.en.srt'
    generator = lambda txt: TextClip(txt,
                                     font='assets/font/GothamMedium.ttf',
                                     fontsize=45, color='white', bg_color='#00000066')
    subtitle = margin(clip=SubtitlesClip(subtitle_path, generator)
                      .set_position(('center', 'bottom')), bottom=35, opacity=0)
    video = VideoFileClip(video_path, audio=True)
    composed_video = CompositeVideoClip([video, subtitle])
    output_filename = 'youtube-output-file'
    composed_video.write_videofile(output_filename, threads=2, fps=video.fps)