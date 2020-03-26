import os
import shutil

import magic


def is_video(path):
    return False if not file_exist(path) else 'video' in magic.from_file(path, mime=True)


def file_exist(path):
    return os.path.exists(path)


def remove_folder(path):
    shutil.rmtree(path, ignore_errors=True)
