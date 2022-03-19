#!/usr/bin/env python

from os import getcwd, path, remove, symlink, unlink
from shutil import rmtree

INSTALL_TYPES = [
    "F", # File
    "D", # Dir
    "L" # Link
]

OPTIONS = [
    "qtile"
]

class OptionNotFound(Exception):
    def __init__(self, options):
        self.options = options
        super().__init__(options)

def welcome():
    print("===================================")
    print(" jppostigo .dotfiles symlink setup ")
    print("===================================")

    option_count = len(OPTIONS)

    print("Select symlinks to install (multiple selection is allowed, separating items by comma):")

    for i in range(option_count):
        print("{}: {}".format(i+1, OPTIONS[i]))

def get_option_selection():
    selected_options = input("> ")
    return [i.strip() for i in selected_options.split(",")]

def check_selected_options_or_raise(selected_options):
    option_errors = []
    
    for option in selected_options:
        if option not in OPTIONS:
            option_errors.append(option)
    
    if option_errors:
        raise OptionNotFound(",".join(option_errors))

def get_install_type(uri):
    if path.islink(uri):
        return "L"
    return "D" if path.isdir(uri) else "F"

def install(options):
    for option in options:
        src_folder = "{}/{}".format(getcwd(), option)
        dest_folder = "{}/.config/{}".format(path.expanduser("~"), option)
        install_type = get_install_type(src_folder) # TODO: implement different types of dotfiles installation (and include the multitype)

        single_install(option, src_folder, dest_folder)

def single_install(option, src, dest, install_type = "L"):

    print("[INSTALLING]", option)
    print(src, "->", dest)

    try:
        symlink(src, dest, True)
    except FileExistsError as e:
        if path.islink(dest):
            print("Symlink for", option, "already exists.")
            install_type = "L"
        elif path.isdir(dest):
            print("Directory for", option, "already exists.")
            install_type = "D"
        elif path.isfile(dest):
            print("File for", option, "already exists.")
            install_type = "F"

        override = input("Override? Everything within your {} folder will be deleted (Y/n) ".format(option))

        if override in ["Y", "y", "S", "s"]:
            print("Overriding dotfiles configuration for", option)
            
            if install_type == "L":
                unlink(dest)
            elif install_type == "D":
                rmtree(dest)
            else:
                remove(dest)
            
            symlink(src, dest, True)
            print("[SUCCESS]", option)
        else:
            print("[SKIP]", option)
    except Exception as e:
        print("Error occurred creating symlink for {}\n{}: {}".format(
            option, type(e), e.args))
        exit()
    else:
        print("[SUCCESS]", option)

def main():
    welcome()
    selected_options = get_option_selection()

    try:
        check_selected_options_or_raise(selected_options)
    except OptionNotFound as option_exception:
        print("Error occurred - option not found:", option_exception.options)
        exit()

    print("Installing symlinks for dotfiles:", ", ".join(selected_options))
    print("======================================================================")
    
    install(selected_options)

if __name__ == "__main__":
    main()
