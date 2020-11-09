import os
import shutil


def is_subtitle(path):
    return False if not file_exist(path) else os.path.splitext(path)[1] in ['.srt']


def file_exist(path):
    return os.path.exists(path)


def remove_folder(path):
    shutil.rmtree(path, ignore_errors=True)


def add_prefix_to_filename(path, prefix):
    file_path, filename_with_extension = os.path.split(path)
    return os.path.join(file_path, f'{prefix}{filename_with_extension}')


def replace_extension(path, extension):
    file_path, filename_with_extension = os.path.split(path)
    filename = os.path.splitext(filename_with_extension)[0]
    return os.path.join(file_path, f'{filename}{extension}')


def is_vtt_subtitle(path):
    file_path, filename_with_extension = os.path.split(path)
    extension = os.path.splitext(filename_with_extension)[1]
    return extension == '.vtt'


def get_filename(path):
    return os.path.basename(path)
