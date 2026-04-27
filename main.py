from modules.handler import handle_answers


def main() -> None:
    print(f"\n{"-"*16} Prototype {"-"*16}")
    print("1. Create a folder")
    print("2. Delete a folder")
    print("3. Delete an empty folder")
    print("4. Go to folder")
    print("99. Quit program")
    # list_dir_helper()
    handle_answers()
    

if __name__ == "__main__":
    while True:
        main() 
