import os
import subprocess


def validate_path(working_directory: str, file_path: str) -> str | None:
    try:
        working_dir_abs = os.path.abspath(working_directory)
        target_path = os.path.normpath(os.path.join(working_dir_abs, file_path))

        target_path_is_within_working_dir = (
            os.path.commonpath([working_dir_abs, target_path]) == working_dir_abs
        )
        if not target_path_is_within_working_dir:
            return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'

        target_is_file = os.path.isfile(target_path)
        if not target_is_file:
            return f'Error: "{file_path}" does not exist or is not a regular file'

        target_is_py_file = file_path[-3:] == ".py"
        if not target_is_py_file:
            return f'Error: "{file_path}" is not a Python file'

    except Exception as e:
        return f"Error: {e}"


# def describe_file(dir: str, file: str):
#     file_path = os.path.join(dir, file)
#     name = file
#     size = os.path.getsize(file_path)
#     is_dir = os.path.isdir(file_path)
#     return f"- {name}: file_size={size} bytes, is_dir={is_dir}"


def run_python_file(
    working_directory: str, file_path: str, args: list[str] | None = None
):
    path_error = validate_path(working_directory, file_path)
    if path_error is not None:
        return path_error
    working_dir_abs = os.path.abspath(working_directory)
    target_abs_path = os.path.join(working_dir_abs, file_path)
    try:
        command = ["python", target_abs_path]
        if args:
            command.extend(args)
        completed_process = subprocess.run(
            command, cwd=working_dir_abs, capture_output=True, text=True, timeout=30
        )
    except Exception as e:
        return f"Error: {e}"

    print("STDERR WAS", repr(completed_process.stderr))
    output = ""
    if completed_process.returncode != 0:
        output += f"Process exited with code {completed_process.returncode}"
    if not completed_process.stderr and not completed_process.stdout:
        output += "No output produced"
    if completed_process.stdout:
        output += f"STDOUT: {completed_process.stdout}"
    if completed_process.stderr:
        output += f"STDERR: {completed_process.stderr}"

    return output
