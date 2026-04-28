from modules.handler import handle_answers


def main() -> None:
    bold = "\033[1m"
    end_bold = "\033[0m"

    print(f"\n{"-"*16} Prototype {"-"*16}")

    print(f"{bold}Folders{end_bold}") 

    print("1. Create a folder")
    print("2. Delete a folder")
    print("3. Delete an empty folder")
    print("4. Go to folder\n")

    print(f"{bold}Files{end_bold}") 
    print("6. Create a file")
    print("7. Delete a file (permanent)\n")

    print("8. Rename folder or file\n")

    print(f"{bold}Combos{end_bold}") 
    print("5. Create and go to - folder\n")
     
    print(f"{bold}Other{end_bold}")
    print("99. Quit program")
    # list_dir_helper()
    handle_answers()


if __name__ == "__main__":
    while True:
        main() 
