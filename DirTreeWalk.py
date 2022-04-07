import argparse
import hashlib
import os
from os.path import join

parser = argparse.ArgumentParser()
parser.add_argument('path', type=str, help='path to show')
args = parser.parse_args()


def printDirectory(f, f_path):
    global sub_files
    fullpath = join(f_path, f)
    if os.path.isfile(fullpath):
        hash_file = hashlib.md5(open(fullpath, 'rb').read()).hexdigest()
        file_info = [f, fullpath, hash_file]
        printBeautiful(file_info)
        return
    elif os.path.isdir(fullpath):
        file_info = [f, '<dir>', '']
        printBeautiful(file_info)
        sub_files = os.listdir(fullpath)
    for subFile in sub_files:
        printDirectory(subFile, fullpath)


def printBeautiful(fileInfo):
    print("{:50} {:50} {:>60}".format(*fileInfo))


if __name__ == '__main__':
    path = args.path
    try:
        dirs = os.listdir(path)
        for file in dirs:
            printDirectory(file, path)
    except PermissionError:
        print('Sie haben keine Berechtiung!')
    except NotADirectoryError:
        print("mich_gibt_es_nicht!")
    except FileNotFoundError:
        print("mich_gibt_es_nicht!")
