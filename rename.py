#!/usr/bin/env python3

'''
File: File Rename
Description:
Created: 2016-08-12
'''



import os
from pathlib import Path
import logging
import magic


# -------------------------------------------------- #
# Script settings
# -------------------------------------------------- #
Testing = False
# set up logging file
logging.basicConfig(filename='log.log', level=logging.INFO, format='%(message)s')

# whether to check files without extensions for their
# mime and then add them automatically if missing.
mimeForce = False

# Check for max length of the file path,
# if it is too long you'll get the option to shorten it,
# this can be useful on NTFS, FAT32 filesystems
LengthCheck = False
# 260 chars max
LengthMax = 260

# run the script for the following directory as the root directory
DirRoot = os.path.expanduser('~')
# these are the directories to exclude, relative to the DirRoot
# e.g. '~/websites' in the list below will exclude the 'websites' folder located in the home directory.
DirExlc = []


print('''
  ____
 |  _ \ ___ _ __   __ _ _ __ ___   ___
 | |_) / _ \ '_ \ / _` | '_ ` _ \ / _ \\
 |  _ <  __/ | | | (_| | | | | | |  __/
 |_| \_\___|_| |_|\__,_|_| |_| |_|\___|
''')



illegal_chars = {
    ('/', '_'),
    ('?', ''),
    ('<', '_'),
    ('>', '_'),
    ('\\', '_'),
    (':', ' - '),
    ('*', '_'),
    ('|', '_'),
    ('’', '\''),
    ('"', ''),
    ('\n', ' ')
}


mimeTypes = {
    'video/mp4': '.mp4',
    'video/x-matroska': '.mkv',
    'application/pdf': '.pdf',
    'application/zip': '.zip',
    'image/png': '.png',
    'text/x-python': '.py',
    'text/plain': '.txt',
    'image/jpeg': '.jpeg',
    'image/webp': '.webp'
}
# ['application/x-java-keystore', 'text/x-makefile', 'text/x-c++', 'image/webp', 'video/mp4', 'application/pdf',
# 'application/x-sqlite3', 'application/x-tex-tfm', 'image/jpeg', 'application/octet-stream', 'application/zip',
# 'text/html', 'application/x-executable', 'inode/x-empty', 'text/x-shellscript', 'application/pgp-keys',
# 'inode/symlink',
# 'text/plain', 'text/x-python']

# -------------------------------------------------- #
#
# -------------------------------------------------- #
def rename(current_path):
    p = Path(current_path)

    # assign the extension is it is a file.
    if mimeForce and str(p.suffix) == '' and os.path.isfile(current_path):
        try:
            mime = magic.from_file(current_path, mime=True)
            mimeCont.append(mime)
        except FileNotFoundError:
            ext = str(p.suffix)
        except OSError:
            ext = str(p.suffix)

        try:
            ext = mimeTypes[mime]
            # skip .txt files
            if ext == '.txt':
                ext = str(p.suffix)
        except KeyError:
            ext = str(p.suffix)
    else:
        ext = str(p.suffix)

    stem = str(p.stem)
    while stem.isspace():
        " ".join(stem.split())
    for chars in illegal_chars:
        stem = stem.replace(chars[0], chars[1])
    new_path = os.path.join(str(p.parent), stem + ext)

    if (os.path.exists(new_path) and new_path != current_path) or (LengthCheck and not len(new_path) <= LengthMax):
        print('Already exits:', stem + ext,
              '\nLenght:', len(new_path),
              '\n@: ', current_path)
        while True:
            stem = input('Enter new stem: ')
            if stem == '!':
                new_path = current_path
                break
            for chars in illegal_chars:
                stem = stem.replace(chars[0], chars[1])
            new_path = os.path.join(str(p.parent), stem + ext)
            if not len(new_path) <= LengthMax:
                print('Length is too long! Try to make is shorter! len:', len(new_path))
            else:
                if not os.path.exists(new_path):
                    break
                else:
                    print('That also exists! Try again!')

    if new_path == current_path:
        return current_path
    else:
        print(current_path + ' -> ' + new_path)
        if not Testing:
            os.rename(current_path, new_path)
        logging.info(current_path + ' -> ' + new_path)
        return new_path


mimeCont, listDirs, listFiles, listDirsExlc = [], [], [], []

if DirExlc:
    for i in DirExlc:
        listDirsExlc.extend([i.replace('~', DirRoot, 1)])

print('Running...')

exclude_prefixes = ['.']
# Generate list of directories.
for root, dirs, files in os.walk(DirRoot, topdown=True):
    dirs[:] = [d for d in dirs if (os.path.join(root, d) not in listDirsExlc)]
    dirs[:] = [d for d in dirs if all([d.startswith(string) is False for string in exclude_prefixes]) is True]
    for dir in dirs:
        listDirs.append(os.path.join(root, dir))

# run for directories
for file in listDirs:
    rename(file)

# Generate list of files.
for root, dirs, files in os.walk(DirRoot, topdown=True):
    dirs[:] = [d for d in dirs if (os.path.join(root, d) not in listDirsExlc)]
    dirs[:] = [d for d in dirs if all([d.startswith(string) is False for string in exclude_prefixes]) is True]
    for filename in files:
        # Join the two strings in order to form the full file path.
        if filename[0] == '.':
            continue
        f = os.path.join(root, filename)
        listFiles.append(f)

# run for files
for file in listFiles:
    rename(file)

print('Done.')