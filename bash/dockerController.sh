#!/bin/bash
## Author:       Alexander Mueller
## Email:        amueller@doctorcrank.de
## Version:      1.3
## Date:         2023-01-20
## Description:  Controll your docker containers
##               Will soon be replaced by a python script

path_dir_docker="/Docker/Docker"
container_list_all=$(for path_file_dockerfile in "${path_dir_docker}/"*"/"*".yml"; do echo "${path_file_dockerfile}" | cut --delimiter='/' --fields='5' | cut --delimiter="." --fields='1'; done | xargs)
container_list_default=$(cat ${path_dir_docker}/container.list)

if [[ "${2}" == '--all' || "${2}" == '-a' ]]
then
	container_list="${container_list_all}"
else
	container_list="${container_list_default}"
fi

if [[ -z "${1}" ]]
then
    echo "No arguments provided, please use down, pull, restart, up or update! Aborting!"
    exit 1
else
    echo "Affected containers: ${container_list}"
fi

for docker_container in ${container_list}
do
	path_file_dockerfile="${path_dir_docker}/${docker_container}/${docker_container}.yml"
	echo "[${docker_container}]"
	case ${1} in
		down)
			docker-compose --file "${path_file_dockerfile}" down
			;;
		pull)
			docker-compose --file "${path_file_dockerfile}" pull
			;;
		restart)
			docker-compose --file "${path_file_dockerfile}" restart
			;;
		up)
			docker-compose --file "${path_file_dockerfile}" up --detach
			;;
		update)
			docker-compose --file "${path_file_dockerfile}" pull
			docker-compose --file "${path_file_dockerfile}" down
			sleep 1
			docker-compose --file "${path_file_dockerfile}" up --detach
			;;
		*)
			echo "Not a valid argument, please use down, pull, restart, up or update!"
			exit 1
	esac
done
