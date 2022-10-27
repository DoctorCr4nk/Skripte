#!/usr/bin/env python3.10
## Author:       Alexander Mueller
## Email:        amueller@doctorcrank.de
## Version:      1.0
## Date:         2022-10-27
## Comment:      In development (actrive)
## Description:  This script will generate a new script based on a template

import argparse
import sys

## Global Variables

header = {}
header_defaults = {
    'author':'None',
    'comment':'new generated script',
    'date':'None',
    'description':'None',
    'email':'foo@bar.com',
    'name':'my_script.sh',
    'shebang':'#!/bin/bash',
    'version':'1.0'}

## Functions

def assign_values(input_values):
    for key in input_values.keys():
        if input_values[key] == None:
            if not generate_missing_values(key):
                header[key] = input_values[key]
        else:           ## Does not make sense
            header[key] = header_defaults[key]

def generate_missing_values(key):
    match key:
        case 'date':
            print('date')
            return True
        case other:
            print('Cannot generate ' + key + ' will use default value ' + header_defaults[key] + ' instead.')
            return False


def main():
    parser = argparse.ArgumentParser(description='This script will generate a new script based on a template. Trying to fill missing values')
    parser.add_argument('-a', '--author')
    parser.add_argument('-c', '--comment')
    parser.add_argument('-d', '--description')
    parser.add_argument('-e', '--email')
    parser.add_argument('-n', '--name', help='Name of the generated script')
    parser.add_argument('-s', '--shebang', default='#!/bin/bash', help='Complete shebang line or keyword like bash')
    parser.add_argument('-v', '--version', default='1.0')

    assign_values(vars(parser.parse_args()))

    print(header)

if __name__ == '__main__':
    sys.exit(main())