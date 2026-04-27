from modules.run_cmd import *


def list_dir_helper() -> None:
    list_dir_result = sp.run(["ls"], text=True, shell=True,
        capture_output=True)
    print("Listing directory...\n", list_dir_result.stdout)


def create_dir(dir_name: str) -> None:
    from modules.handler import handle_empty_name
    handle_empty_name(dir_name)
    run_cmd(f"mkdir {dir_name}")
    list_dir_helper()


def remove_dir(dir_name: str) -> None:
    from modules.handler import handle_empty_name
    handle_empty_name(dir_name)
    run_cmd(f"rm -r {dir_name}")
    list_dir_helper()


def change_cd(existing_dir: str) -> None:
    from modules.handler import handle_empty_name
    handle_empty_name(existing_dir)
    run_cmd(f"cd {existing_dir}")
    list_dir_helper()
