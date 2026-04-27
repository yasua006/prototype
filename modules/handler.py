import sys

from modules.dirs import *
from modules.files import *


def handle_empty_name(name: str):
    if not name:
        print("Empty or invalid name! Exiting...")
        sys.exit(1)


def handle_answers() -> None:
    try:
        choice: int = int(input("Choice: "))
    except Exception:
        choice = 0

    match choice:
        case 1:
            dir_name: str = input("Folder name to add: ")
            create_dir(dir_name)
        case 2:
            dir_name: str = input("Folder name to delete: ")
            remove_dir(dir_name)
        case 3:
            dir_name: str = input("Empty folder name to delete: ")
            remove_empty_dir(dir_name)
        case 4:
            existing_dir: str = input("Existing folder name: ")
            change_cd(existing_dir)
        case 5:
            dir_name: str = input("Folder name to add and go to: ")
            create_change_dir(dir_name)
        case 6:
            file_name: str = input("File name to add: ")
            create_file(file_name)
        case 7:
            file_name: str = input("File name to delete: ")
            remove_file(file_name)
        case 99:
            print("You quit program.")
            sys.exit(1)
        case _:
            print("Invalid option! Please try again!\n")
