__winc_id__ = "ae539110d03e49ea8738fd413ac44ba8"
__human_name__ = "files"

import os
from zipfile import ZipFile

# def clean_cache():
#     path = 'files/cache'
#     if os.path.isdir(path):
#         for file_name in os.listdir(path):
#             os.remove(path + '/' + file_name)
#     else:
#         os.mkdir(path)

# clean_cache()

def cache_zip(zipfile_path, cache_dir):
    with ZipFile(zipfile_path) as myZip:
        myZip.extractall(cache_dir, members=None, pwd=None)

# cache_zip('files/data.zip', 'files/cache')

# def cached_files():
#     files = []
#     for filename in os.listdir('files/cache'):
#         file_path = os.path.abspath(filename)
#         if not filename in files:
#                 files.append(file_path)
#     return files

# print(cached_files())

def cached_files():
    path = 'files/cache'
    files = []
    for file in os.listdir(path):
            if os.path.isfile(os.path.join(path, file)):
                file_path = os.path.abspath(file)
                if not file_path in files:
                    files.append(file_path)
    return files

print(cached_files())