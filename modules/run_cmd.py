import subprocess as sp
from subprocess import CompletedProcess


def run_cmd(cmd_to_run, working_dir: str | None) -> CompletedProcess[str]:
    return sp.run([cmd_to_run], text=True, shell=True,
        cwd=working_dir)
