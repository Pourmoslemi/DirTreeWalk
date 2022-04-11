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
    """
    This function traverses a directory tree (incl. the subdirectories -- i.e. recursively). 
    Determine the MD5 sum for each entry found. The programme should output the file name, 
    the file path (relative to the start directory) and the MD5 sum (only for the file) 
    on the standard output for each entry found.
    """
    global sub_files
    # Join various path components
    fullpath = join(path, f)
    # Check whether the 
    # specified path is 
    # an existing file
    if os.path.isfile(fullpath):
        # If the file exists, the MD5 sum of the file is determined.
        hash_file = hashlib.md5(open(fullpath, 'rb').read()).hexdigest()
        # Compute the relative file path to the 
        # given path from the the current directory.
        rel_pass = os.path.relpath(fullpath)
        # Create a list from file information
        file_info = [f, rel_pass, hash_file]
        # Call the function printBeautiful to output the information as a table.
        printBeautiful(file_info)
        return
#   elif os.path.isdir(fullpath):
    else:
        # Create a list if it is a folder
        file_info = [f, '<dir>', '']
        # Call the function printBeautiful to output the information as a table.
        printBeautiful(file_info)
        sub_files = os.listdir(fullpath)
    for subFile in sub_files:
        dirtreewalk(subFile, fullpath)


def printBeautiful(fileInfo):
    print("{:50} {:50} {:>60}".format(*fileInfo))
    

# Python program to use
# main for function call.
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
