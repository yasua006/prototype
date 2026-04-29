from modules.run_cmd import *

working_dir = None


def list_dir_helper() -> None:
    list_dir_result = sp.run(["ls"], text=True, shell=True,
        capture_output=True, cwd=working_dir)
    print("Listing directory...\n",
        list_dir_result.stdout or "Folder is empty")


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
    global working_dir
    working_dir = existing_dir

    from modules.handler import handle_empty_name
    handle_empty_name(existing_dir)
    list_dir_helper()


def create_change_dir(dir_name: str) -> None:
    create_dir(dir_name)
    change_cd(dir_name)


def move_dir(source: str, target: str) -> None:
    from modules.handler import handle_empty_name
    handle_empty_name(source)
    handle_empty_name(target)
    run_cmd(f"mv {source} {target}", working_dir)
    list_dir_helper()
