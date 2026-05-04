from modules.bold_unicodes import *
from modules.handler import handle_answers
from modules.dirs import list_dir_helper



def main() -> None:
    print(f"\n{"-"*16} Prototype {"-"*16}")

    print(f"{bold}Folders and Files{end_bold}") 

    print("1a. Create folder(s)")
    print("1b. Create file(s)\n")

    print("2a. Delete folder(s)")
    print("2b. Delete file(s) [permanent]\n")

    print("3. Delete empty folder(s)\n")

    print("4. Go to folder\n")

    print("5a. Move folder")
    print("5b. Move file(s)\n")

    print("6. Rename folder or file\n")

    print(f"{bold}Combos{end_bold}") 
    print("7. Create and go to - folder\n")
     
    print(f"{bold}Other{end_bold}")
    print("99. Quit program\n")

    list_dir_helper()

    handle_answers()


if __name__ == "__main__":
    while True:
        main() 
