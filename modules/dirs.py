from modules.run_cmd import *
from modules.bold_unicodes import *
from modules import shortcuts

working_dir = None

log_file = open("log.txt", "a+")


def list_dir_helper() -> None:
    list_dir_result = sp.run(["ls"], text=True, shell=True,
        capture_output=True, cwd=working_dir)

    folder_name = sp.run(
        ['basename "$(pwd)"'], text=True, shell=True,
        capture_output=True, cwd=working_dir
    )

    print(
        f"\n{bold}Current folder: {folder_name.stdout.strip()}{end_bold}\n {list_dir_result.stdout or "Folder is empty"}"
    )
    print("\n")


# fungerer for flere mapper også
def create_dir(dir_name: str) -> None:
    from modules.handler import handle_empty_name
    handle_empty_name(dir_name)
    run_cmd(f"mkdir {dir_name}", working_dir)
    list_dir_helper()


def remove_dir(dir_name: str) -> None:
    from modules.handler import handle_empty_name
    handle_empty_name(dir_name)
    run_cmd(f"rm -r {dir_name}", working_dir)
    list_dir_helper()

def remove_empty_dir(dir_name: str) -> None:
    from modules.handler import handle_empty_name
    handle_empty_name(dir_name)
    run_cmd(f"rmdir {dir_name}", working_dir)
    list_dir_helper()


def change_cd(existing_dir: str) -> None:
    cuts: str = existing_dir.lower().strip()

    global working_dir
    log_file.write(f"\nPrevious working dir. {working_dir or "program default path"}\n")

    match cuts: 
        case shortcuts.docs:
            print("Documents shortcut")
            working_dir = "Documents"
            log_file.write(f"Working dir: {working_dir}\n")
        case shortcuts.desk:
            print("Desktop shortcut")
            working_dir = "Desktop"
            log_file.write(f"Working dir: {working_dir}\n")
        case _:
            working_dir = existing_dir

            from modules.handler import handle_empty_name
            handle_empty_name(existing_dir)

    list_dir_helper()
    # log_file.close()


def create_change_dir(dir_name: str) -> None:
    create_dir(dir_name)
    change_cd(dir_name)


def show_current_dir() -> None:
    list_dir_helper()
