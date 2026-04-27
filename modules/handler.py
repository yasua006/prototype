import sys

from modules.dirs import create_dir, remove_dir, change_cd


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
            existing_dir: str = input("Existing folder name: ")
            change_cd(existing_dir)
        case 99:
            print("You quit program.")
            sys.exit(1)
        case _:
            print("Invalid option! Please try again!\n")
