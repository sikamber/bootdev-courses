import os


def validate_path(working_directory: str, directory: str) -> str | None:
    try:
        working_dir_abs = os.path.abspath(working_directory)
        target_dir = os.path.normpath(os.path.join(working_dir_abs, directory))

        target_dir_is_within_working_dir = (
            os.path.commonpath([working_dir_abs, target_dir]) == working_dir_abs
        )
        if not target_dir_is_within_working_dir:
            return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'

        target_dir_is_directory = os.path.isdir(target_dir)
        if not target_dir_is_directory:
            return f'Error: "{directory}" is not a directory'

    except Exception as e:
        return f"Error: {e}"


def describe_file(dir: str, file: str):
    file_path = os.path.join(dir, file)
    name = file
    size = os.path.getsize(file_path)
    is_dir = os.path.isdir(file_path)
    return f"- {name}: file_size={size} bytes, is_dir={is_dir}"


def get_files_info(working_directory: str, directory: str = "."):
    path_error = validate_path(working_directory, directory)
    if path_error is not None:
        return path_error
    target_dir = os.path.join(working_directory, directory)
    file_descriptions = [
        describe_file(target_dir, file) for file in os.listdir(target_dir)
    ]
    return "\n".join(file_descriptions)
