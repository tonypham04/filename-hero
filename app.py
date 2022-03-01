import os
import re

def main():
    """The main function which executes the script"""
    files = os.listdir()
    remove_spaces(files, '-')

def get_unhidden_files_only(all_files: list[str]) -> list[str]:
    """This function accepts a list of filenames and returns a new list of filenames excluding hidden files."""
    # List comprehension which returns the list of files without ones beginning with a '.' (i.e. hidden files)
    return [file for file in all_files if not file.startswith('.')]

def remove_spaces(all_files: list[str], delimiter: str, exclude_hidden_files=True) -> None:
    """This function replaces spaces in a list of filenames with a specified delimiter"""
    if exclude_hidden_files:
        all_files = get_unhidden_files_only(all_files)
    for file in all_files:
        # Regex expression to replace all instances of spaces with the specified delimeter
        new_name = re.sub(r'\s', delimiter, file)
        os.rename(file, new_name)

# This is a useful guard to ensure code is only executed when it is being run as the main program and not when imported into another module
if __name__ == '__main__':
    main()