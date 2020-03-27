import glob

from utils.file_utils import is_video, is_subtitle
from video.video_edit import add_subtitle


def generate_video_with_subtitle():
    video_path = next(path for path in glob.glob('download/*') if is_video(path))
    subtitle_path = next(path for path in glob.glob('download/*') if is_subtitle(path))
    add_subtitle(video_path, subtitle_path)

