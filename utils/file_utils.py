import os

import magic


def is_video(path):
    return False if file_exist(path) else 'video' in magic.from_file(path, mime=True)


def file_exist(path):
    return os.path.exists(path)
