import sys

from modules.dirs import *
from modules.files import *
from modules.rename import *


def handle_empty_name(name: str):
    if not name:
        print("Empty or invalid name! Exiting...")
        sys.exit(1)


def handle_answers() -> None:
    choice: str = input("Choice: ")

    match choice:
        case "1a":
            dir_name: str = input("Folder name(s) to add (separated by space): ")
            create_dir(dir_name)
        case "1b":
            file_name: str = input("File name to add: ")
            create_file(file_name)
        case "2a":
            dir_name: str = input("Folder name to delete: ")
            remove_dir(dir_name)
        case "2b":
            file_name: str = input("File name to delete: ")
            remove_file(file_name)
        case "3":
            dir_name: str = input("Empty folder name to delete: ")
            remove_empty_dir(dir_name)
        case "4":
            existing_dir: str = input("Existing folder name: ")
            change_cd(existing_dir)
        case "5a":
            source: str = input("Folder name to move: ")
            target: str = input("Folder name to move to: ")
            move_dir(source, target)
        case "5b":
            source: str = input("File name to move: ")
            target: str = input("Folder name to move file to: ")
            move_file(source, target)
        case "6":
            old_name: str = input("Current folder or file name: ")
            new_name: str = input("New folder or file name: ")
            rename(old_name, new_name)
        case "7":
            dir_name: str = input("Folder name to add and go to: ")
            create_change_dir(dir_name)
        case "99":
            print("You quit program.")
            sys.exit(1)
        case _:
            print("Invalid option! Please try again!\n")
