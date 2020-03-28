from typing import Any, Callable

from moviepy.video.VideoClip import TextClip
from moviepy.video.compositing.CompositeVideoClip import CompositeVideoClip
from moviepy.video.io.VideoFileClip import VideoFileClip
from moviepy.video.tools.subtitles import SubtitlesClip

from utils.file_utils import add_prefix_to_filename, replace_extension


def add_subtitle(video_path, subtitle_path, filename=None):
    generator: Callable[[Any], TextClip] = lambda txt: TextClip(txt,
                                                                font='./GothamMedium.ttf',
                                                                fontsize=35, color='white',
                                                                bg_color='#00000066')
    subtitle = SubtitlesClip(subtitle_path, generator).margin(bottom=15, opacity=0).set_position(('center', 'bottom'))
    video = VideoFileClip(video_path, audio=True)
    composed_video = CompositeVideoClip([video, subtitle])
    output_filename = filename or replace_extension(add_prefix_to_filename(video_path, '[WITH-SUBTITLE] '), '.mp4')
    composed_video.write_videofile(output_filename,
                                   threads=4,
                                   fps=video.fps)
