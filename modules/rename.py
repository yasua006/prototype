from modules.files import working_dir, run_cmd, list_dir_helper


def rename(old_name: str, new_name: str) -> None:
    from modules.handler import handle_empty_name
    handle_empty_name(old_name)
    handle_empty_name(new_name)
    run_cmd(f"mv {old_name} {new_name}", working_dir)
    list_dir_helper()
