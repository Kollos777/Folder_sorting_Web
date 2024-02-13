from pathlib import Path
import os
import shutil
import sys
from threading import Thread


def processing_folder(path):

    for directory in path.iterdir():
        
        if directory.is_dir():
            if directory in files:
                continue
            try:
                os.rmdir(directory)
                continue
            except OSError:
                thread = Thread(target=processing_folder, args=(directory,))
                thread.start()
                continue
        files.append(directory)

    return files

def processing_file(file):
    remove_extension = file.suffix[1:]
    os.mkdir(remove_extension)
    shutil.move(file, remove_extension)


def root_dir():
    if len(sys.argv) != 2:
        print("No argument")
        return sys.exit(1)
    elif not Path(sys.argv[1]).exists():
        print("Does not exist")
        return sys.exit(1)

    return Path(sys.argv[1])



def main():
    path = root_dir()
    os.chdir(path)

    for dir in files:
        try:
            os.mkdir(dir)
        except FileExistsError:
            continue

    processing_folder(path)
    print(files)
    for file in files:
        thread = Thread(target=processing_file, args=(file,))
        thread.start()


famous = set()
unknown = set()
files = []

if __name__ == "__main__":
    main()