import os


def validate_path(working_directory: str, file_path: str) -> str | None:
    try:
        working_dir_abs = os.path.abspath(working_directory)
        target_path = os.path.normpath(os.path.join(working_dir_abs, file_path))

        target_path_is_within_working_dir = (
            os.path.commonpath([working_dir_abs, target_path]) == working_dir_abs
        )
        if not target_path_is_within_working_dir:
            return f'Error: Cannot write to "{file_path}" as it is outside the permitted working directory'

        target_is_directory = os.path.isdir(target_path)
        if target_is_directory:
            return f'Error: Cannot write to "{file_path}" as it is a directory'

    except Exception as e:
        return f"Error: {e}"


# def describe_file(dir: str, file: str):
#     file_path = os.path.join(dir, file)
#     name = file
#     size = os.path.getsize(file_path)
#     is_dir = os.path.isdir(file_path)
#     return f"- {name}: file_size={size} bytes, is_dir={is_dir}"


def write_file(working_directory: str, file_path: str, content: str):
    path_error = validate_path(working_directory, file_path)
    if path_error is not None:
        return path_error
    target_path = os.path.join(working_directory, file_path)
    os.makedirs(target_path[: target_path.rindex("/")], exist_ok=True)
    try:
        with open(target_path, "w") as f:
            f.write(content)
    except Exception as e:
        return f"Error: {e}"

    return f'Successfully wrote to "{file_path}" ({len(content)} characters written)'
