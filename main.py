import glob
import os

from moviepy.video.VideoClip import TextClip
from moviepy.video.compositing.CompositeVideoClip import CompositeVideoClip
from moviepy.video.fx.margin import margin
from moviepy.video.io.VideoFileClip import VideoFileClip
from moviepy.video.tools.subtitles import SubtitlesClip

from youtube.youtube import fetch_youtube_feed_entries

entries = fetch_youtube_feed_entries()

os.system(f'you-get --output-filename youtube-download-file https://www.youtube.com/watch?v={entries[2].video_id}')
video_path = next((path for path in glob.glob('youtube-download-file.*')), None)
subtitle_path = next((path for path in glob.glob('*.srt')), None)
print('video_path', video_path)
print('subtitle_path', subtitle_path)
generator = lambda txt: TextClip(txt,
                                 font='assets/font/GothamMedium.ttf',
                                 fontsize=45, color='white', bg_color='#00000066')
subtitle = margin(clip=SubtitlesClip(subtitle_path, generator)
                  .set_position(('center', 'bottom')), bottom=35, opacity=0)
video = VideoFileClip(video_path, audio=True)
composed_video = CompositeVideoClip([video, subtitle])
output_filename = 'youtube-output-file'
composed_video.write_videofile(output_filename, threads=2, fps=video.fps)