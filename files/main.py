__winc_id__ = "ae539110d03e49ea8738fd413ac44ba8"
__human_name__ = "files"

import os
from zipfile import ZipFile

cache_folder = os.path.join('files', 'cache')
PATH = os.path.join(os.getcwd(), cache_folder)

def clean_cache():
    if os.path.isdir(PATH):
        for file_name in os.listdir(PATH):
            print(file_name)
            os.remove(os.path.join(PATH, file_name))
    else:
        os.mkdir(PATH)


def cache_zip(zipfile_path, cache_dir):
    with ZipFile(zipfile_path) as myZip:
        myZip.extractall(cache_dir, members=None, pwd=None)


def cached_files():
    files = []
    for file in os.listdir(PATH):
            file_path = os.path.join(PATH, file)
            if os.path.isfile(file_path):
                if not file_path in files:
                    files.append(file_path)
    return files


def find_password(filelist):
    string = 'password'
    for file in filelist:
        open_file = open(file, "r")
        lines = open_file.readlines()
        for line in lines:
            if string in line:
                open(file, "r").close()
                return line[line.find(" ")+1:-1]


if __name__ == "__main__":
    clean_cache()
    # cache_zip('files/data.zip', PATH)
    # print(cached_files()) 
    # print(find_password(cached_files()))



