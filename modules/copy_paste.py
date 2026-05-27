from modules.files import working_dir, run_cmd, list_dir_helper


def copy_paste(old_name: str, new_name: str) -> None:
    from modules.handler import handle_empty_name
    handle_empty_name(old_name)
    handle_empty_name(new_name)
    run_cmd(f"cp {old_name} {new_name}", working_dir)
    list_dir_helper()
