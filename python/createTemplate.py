#!/usr/bin/python3.10
## Author:       Alexander Mueller
## Email:        amueller@doctorcrank.de
## Version:      1.1
## Date:         2023-02-27
## Description:  This script will generate a new script template

import argparse
import sys
from datetime import date

## Global Variables
header = {
    'date' : str(date.today()),
    'shebang' : ''
    }
header_defaults = {
    'author' : 'Alexander Mueller',
    'description' : 'None',
    'email' : 'amueller@doctorcrank.de',
    'file_extensions' : {
        'sh' : 'bash',
        'py' : 'python3'},
    'shebang' : {
        'bash' : '#!/bin/bash',
        'python3' : '#!/usr/bin/python3'},
    'version' : '1.0'}

## Functions
def assign_values(input_values):
    for key in input_values.keys():
        if not input_values[key]:
            if key not in ["name", "shebang"]:
                header[key] = header_defaults[key]
            if key == "shebang":
                for file_extension in header_defaults["file_extensions"]:
                    if file_extension == input_values["name"].split(".")[-1]:
                        script_type = header_defaults["file_extensions"][file_extension]
                        header['shebang'] = header_defaults["shebang"][script_type]
                if not header["shebang"]:
                    print("Cannot generate shebang for a ." + input_values["name"].split(".")[-1] + " script")
                    header.pop('shebang', None)
        else:
            header[key] = input_values[key]

def create_script():
    try:
        new_script = open(header["name"], "xt")
    except:
        print("File already exists.", end=" ")
        answer = input ("Overwrite? [y/n] ")
        if answer.lower() in ["y","yes"]:
            try:
                new_script = open(header["name"], "w")
            except:
                print("Cannot write to file, abort")
                exit(3)
        elif answer.lower() in ["n","no"]:
            exit(1)
        else:
            print("Only yYnNyesno are valid options!")
            exit(2)
    if "shebang" in header.keys():
        new_script.write(header["shebang"] + "\n")
    new_script.close()
    new_script = open(header["name"], "a")
    for key in header.keys():
        if not key == "shebang":
            if len(key) <= 5:
                spacer = "\t\t"
            else:
                spacer = "\t"
            new_script.write("# " + key + spacer + header[key] + "\n")
    new_script.close()
    print("Created the script: " + header["name"])

def main():
    parser = argparse.ArgumentParser(description='This script will generate a new script based on a template. Trying to fill missing values')
    parser.add_argument('-a', '--author')
    parser.add_argument('-d', '--description')
    parser.add_argument('-e', '--email')
    parser.add_argument('-n', '--name', help='Name of the generated script', required=True)
    parser.add_argument('-s', '--shebang', help='Complete shebang line or keyword like bash')
    parser.add_argument('-v', '--version')
    assign_values(vars(parser.parse_args()))
    create_script()

if __name__ == '__main__':
    sys.exit(main())
