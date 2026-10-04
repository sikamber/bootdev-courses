import os


def validate_path(working_directory: str, file_path: str) -> str | None:
    try:
        working_dir_abs = os.path.abspath(working_directory)
        target_path = os.path.normpath(os.path.join(working_dir_abs, file_path))

        target_path_is_within_working_dir = (
            os.path.commonpath([working_dir_abs, target_path]) == working_dir_abs
        )
        if not target_path_is_within_working_dir:
            return f'Error: Cannot read "{file_path}" as it is outside the permitted working directory'

        target_is_file = os.path.isfile(target_path)
        if not target_is_file:
            return f'Error: File not found or is not a regular file: "{file_path}"'

    except Exception as e:
        return f"Error: {e}"


def describe_file(dir: str, file: str):
    file_path = os.path.join(dir, file)
    name = file
    size = os.path.getsize(file_path)
    is_dir = os.path.isdir(file_path)
    return f"- {name}: file_size={size} bytes, is_dir={is_dir}"


def get_file_content(working_directory: str, file_path: str):
    path_error = validate_path(working_directory, file_path)
    if path_error is not None:
        return path_error
    target_path = os.path.join(working_directory, file_path)
    with open(target_path, "r") as f:
        content = f.read(10000)
        if f.read(1):
            content += f'[...File "{file_path}" truncated at 10.000 characters]'

    return content
