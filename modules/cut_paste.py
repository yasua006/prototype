from modules.dirs import working_dir, run_cmd, list_dir_helper

def move(source: str, target: str) -> None:
    from modules.handler import handle_empty_name
    handle_empty_name(source)
    handle_empty_name(target)
    run_cmd(f"mv {source} {target}", working_dir)
    list_dir_helper()
