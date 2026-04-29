from modules.dirs import working_dir, run_cmd, list_dir_helper


def create_file(file_name: str) -> None:
    from modules.handler import handle_empty_name
    handle_empty_name(file_name)
    run_cmd(f"touch {file_name}", working_dir)
    list_dir_helper()


def remove_file(file_name: str) -> None:
    from modules.handler import handle_empty_name
    handle_empty_name(file_name)
    run_cmd(f"rm {file_name}", working_dir)
    list_dir_helper()


def move_file(source: str, target: str) -> None:
    from modules.handler import handle_empty_name
    handle_empty_name(source)
    handle_empty_name(target)
    run_cmd(f"mv {source} {target}", working_dir)
    list_dir_helper()
