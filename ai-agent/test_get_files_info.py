import textwrap

from functions.get_files_info import get_files_info


def indented_files_info(*args):
    return textwrap.indent(get_files_info(*args), "  ")


if __name__ == "__main__":
    print("Result for current directory:")
    print(indented_files_info("calculator", "."))
    print("Result for 'pkg' directory:")
    print(indented_files_info("calculator", "pkg"))
    print("Result for '/bin' directory:")
    print(indented_files_info("calculator", "/bin"))
    print("Result for '../' directory:")
    print(indented_files_info("calculator", "../"))
