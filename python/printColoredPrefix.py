#!/usr/bin/python3
## author		    Alexander Mueller
## email			amueller@doctorcrank.de
## date			    2023-03-28
## version		    1.0
## description		print colored keyword before message

import argparse

class text_color:
    ABORT   = '\033[41m'
    DEBUG   = '\033[94m'
    ERROR   = '\033[91m'
    NOCOLOR = '\033[0m'
    SUCCESS = '\033[36m'
    WARNING = '\033[93m'
    WHYRUN  = '\033[32m'

def get_longest_string_length(string_list: list) -> int:
    string_length = int()
    for string in string_list:
        if len(string) > string_length:
            string_length = len(string)
    return string_length

def main():
    global verbosity
    arguments = parse_arguments()
    verbosity = {
        "quiet"     : arguments["quiet"],
        "verbose"   : arguments["verbose"],
        "whyrun"    : arguments["whyrun"]
    }
    print(arguments)

def parse_arguments() -> dict:
    main_parser = argparse.ArgumentParser(description="Hello I print colored text")
    main_parser.add_argument("-q", "--quiet", action="store_true", default=False, help="Suppress Output")
    main_parser.add_argument("-v", "--verbose", action="store_true", default=False, help="Print debug messages")
    main_parser.add_argument("-w", "--whyrun", action="store_true", default=False, help="Print what would be done")
    arguments = vars(main_parser.parse_args())
    if arguments["quiet"] and arguments["verbose"]:
        print_prefix("ABORT", "You can't use quiet and verbose at the same time!", 1)
    return arguments

def print_prefix(prefix: str, message: str = None, exit_code: int = None, newline: bool = True):
    prefixes = ["ABORT", "DEBUG", "ERROR", "OUTPUT", "SUCCESS", "WARNING", "WHYRUN"]
    prefix_box_length = get_longest_string_length(prefixes)
    if prefix not in prefixes:
        print_prefix("WARNING", "Unknown prefix: " + prefix + " Please use one of these instead:")
        for available_prefix in prefixes:
            print(available_prefix, end="")
            if not available_prefix == prefixes[-1]:
                print(", ", end="")
        print()

if __name__ == '__main__':
    main()
