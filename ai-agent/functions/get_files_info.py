import os


def get_files_info(working_directory: str, directory: str = "."):
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

        return f'Success: "{directory}" is within the working directory'
    except Exception as e:
        return f"Error: {e}"

    print(working_dir_abs)


get_files_info("calculator")
