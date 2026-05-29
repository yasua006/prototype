from pick import pick

from modules.bold_unicodes import *
from modules.dirs import list_dir_helper



def main() -> None:
    from modules.handler import handle_answers

    title = f"\n{"-"*16} Prototype {"-"*16}"
    options = [
        "Create folder(s)", "Create file(s)",
        "Delete folder(s)", "Delete file(s) [permanent]",
        "Delete empty folder(s)",
        "Go to folder",
        "Rename folder(s) or file(s)",
        "Copy and paste folder(s) or file(s)",
        "Cut and paste folder(s) or file(s)",
        "Create and go to - folder",
        "Quit program"
    ]
    choice, index = pick(options, title, indicator="->")

    # print(f"{bold}Folders and Files{end_bold}") 
    # print(f"{bold}Combos{end_bold}") 
    # print(f"{bold}Other{end_bold}")

    list_dir_helper()

    handle_answers(options, choice)


if __name__ == "__main__":
    while True:
        main() 
