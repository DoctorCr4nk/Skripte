#!/usr/bin/python3.10
## author		    Alexander Mueller
## email			amueller@doctorcrank.de
## date			    2023-02-27
## version		    1.3
## description		Manage your docker containers at once

import argparse

import subprocess
import sys
import os
from datetime import date

path_dir_docker_compose_root="/Docker/Docker"

def check_if_compose_exists(container):
    path_file_compose = path_dir_docker_compose_root + "/" + container + "/" + container + ".yml"
    try:
        file_compose = open(path_file_compose, "rt")
    except:
        print("Cannot read docker-compose file of container: " + container)
        exit(3)

def dc_start(container_list):

    pass

def dc_down(container_list):
    pass

def dc_pull(container_list):
    pass

def dc_restart(container_list, mode=None):
    pass

def dc_update(container_list):
    dc_pull(container_list)
    pass

def get_container_list(get_all):
    container_list = []
    path_file_container_list = path_dir_docker_compose_root + "/container.list"
    if not os.path.isdir(path_dir_docker_compose_root):
        print("Docker-compose root dir does not exist, please check the path_dir_docker_compose_root variable in this script. Abort")
        exit(1)
    if get_all:
        for container in os.listdir(path_dir_docker_compose_root):
            path_file_compose = path_dir_docker_compose_root + "/" + container + "/" + container + ".yml"
            if os.path.isfile(path_file_compose):
                try:
                    file_compose = open(path_file_compose, "rt")
                    container_list.append(container)
                    file_compose.close()
                except:
                    print("Cannot open compose file of " + container)
                    exit(4)

    else:
        try:
            file_container_list = open(path_file_container_list, "rt")
            for container in file_container_list.read().split():
                container_list.append(container)
            file_container_list.close
        except:
            print("Cannot open container list")
            exit(2)
    return container_list

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Manage your docker containers at once')
    parser.add_argument('-a', '--all', action='store_true', help="Will affect all docker containers")
    parser.add_argument('-c', '--containers', help="Will affect only these docker containers. Comma seperated list")
    parser.add_argument('-d', '--down', action='store_true', help="Will stop docker containers")
    parser.add_argument('-l', '--list', action='store_true', help="Just list the selected containers")
    parser.add_argument('-p', '--pull', action='store_true', help="Pull new images")
    parser.add_argument('-r', '--restart', action='store_true', help="restart the containers")
    parser.add_argument('--restart-hard', action='store_true', help="Stop and Start containers, not using the docker-compose restart")
    parser.add_argument('-s', '--start', '--up', action='store_true', help="Start the docker containers")
    parser.add_argument('-u', '--update', action='store_true', help="Pull new images and hard restart container with updates available")
    args = vars(parser.parse_args())

    if args["containers"]:
        container_list = args["containers"].split(",")
    else:
        container_list = get_container_list(args["all"])
    for container in container_list:
        check_if_compose_exists(container)

    if args["down"]:
        dc_down(container_list)
        exit(0)

    if args["list"]:
        print("Affected containers: ", end="")
        for container in container_list:
            print(container, end=" ")
        print()
        exit(0)

    if args["pull"]:
        dc_pull(container_list)
        exit(0)

    if args["restart"]:
        dc_restart(container_list)
        exit(0)

    if args["restart_hard"]:
        dc_restart(container_list, "hard")
        exit(0)

    if args["start"]:
        dc_start(container_list)
        exit(0)

    if args["update"]:
        dc_update(container_list)
        exit(0)

exit(0)
import subprocess

# Define the command to run
command = ["docker-compose", "up"]

# Run the command as a subprocess
process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

# Wait for the subprocess to finish and get the output
stdout, stderr = process.communicate()

# Print the output
print(stdout.decode())
