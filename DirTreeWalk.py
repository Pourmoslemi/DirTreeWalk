import argparse
import hashlib
import os
from os.path import join

# Create the parser
parser = argparse.ArgumentParser()
# Add the arguments
parser.add_argument('path', type=str, help='path to show')
# Execute the parse_args() method
args = parser.parse_args()


def dirtreewalk(f, path):
    global sub_files
    fullpath = join(path, f)
    if os.path.isfile(fullpath):
        hash_file = hashlib.md5(open(fullpath, 'rb').read()).hexdigest()
        rel_pass = os.path.relpath(fullpath)
        file_info = [f, rel_pass, hash_file]
        printBeautiful(file_info)
        return
    elif os.path.isdir(fullpath):
        file_info = [f, '<dir>', '']
        printBeautiful(file_info)
        sub_files = os.listdir(fullpath)
    for subFile in sub_files:
        dirtreewalk(subFile, fullpath)


def printBeautiful(fileInfo):
    print("{:50} {:50} {:>60}".format(*fileInfo))


if __name__ == '__main__':
    input_path = args.path
    if not os.path.isdir(input_path):
        print('mich_gibt_es_nicht!')
    else:
        try:
            dirs = os.listdir(input_path)
            for file in dirs:
                dirtreewalk(file, input_path)
        except PermissionError:
            print('Sie haben keine Berechtiung!')
        except NotADirectoryError:
            print("mich_gibt_es_nicht!")
        except FileNotFoundError:
            print("mich_gibt_es_nicht!")
