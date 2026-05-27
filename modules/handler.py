import sys

from modules.dirs import *
from modules.files import *
from modules.rename import *
from modules.cut_paste import *
from modules.copy_paste import *


def handle_empty_name(name: str) -> None:
    if not name:
        print("Empty or invalid name! Exiting...")
        sys.exit(1)


def handle_answers(options: list[str], choice) -> None:
    if choice == options[0]:
        dir_name: str = input("Folder name(s) to add (separated by space): ")
        create_dir(dir_name)
    if choice == options[1]:
        file_name: str = input("File name(s) to add (separated by space): ")
        create_file(file_name)
    if choice == options[2]:
        dir_name: str = input("Folder name(s) to delete (separated by space): ")
        remove_dir(dir_name)
    if choice == options[3]:
        file_name: str = input("File name(s) to delete (separated by space): ")
        remove_file(file_name)
    if choice == options[4]:
        dir_name: str = input("Empty folder name(s) to delete (separated by space): ")
        remove_empty_dir(dir_name)
    if choice == options[5]:
        existing_dir: str = input("Existing folder name: ")
        change_cd(existing_dir)
    if choice == options[6]:
        source: str = input("Folder or file name to cut: ")
        target: str = input("Location to paste cut: ")
        move(source, target)
    if choice == options[7]:
        old_name: str = input("Current folder or file name: ")
        new_name: str = input("New folder or file name: ")
        rename(old_name, new_name)
    if choice == options[8]:
        copy: str = input("Folder or file name to copy: ")
        paste_loc: str = input("Location to paste copied: ")
        copy_paste(copy, paste_loc)
    if choice == options[9]:
        dir_name: str = input("Folder name to add and go to: ")
        create_change_dir(dir_name)
    if choice == options[10]:
        print("You quit program.")
        sys.exit(1)
    
    print("Invalid option! Please try again!\n")
