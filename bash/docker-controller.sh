#!/bin/bash
## Author:       Alexander Mueller
## Email:        amueller@doctorcrank.de
## Version:      1.1
## Date:         2022-12-16
## Description:  Controll your docker containers

path_docker="/home/amueller/Docker"
container_list_all=$(for dockerfile in $(ls "${path_docker}/"*"/"*".yml"); do echo "${dockerfile}" | cut --delimiter='/' --fields='5'; done)
container_list_default="changedetection grafana heimdall redmine smokeping"

if [[ "${2}" == '--all' || "${2}" == '-a' ]]
then
	container_list="${container_list_all}"
else
	container_list="${container_list_default}"
fi
echo "Affected containers: ${container_list}"

case ${1} in
	down)
		echo "Stopping docker containers"
		for service in ${container_list}
		do
				docker-compose --file "${path_docker}/${service}/${service}.yml" down
		done
		;;
	pull)
		echo "Pulling docker images"
		for service in ${container_list}
		do
				docker-compose --file "${path_docker}/${service}/${service}.yml" pull
		done
		;;
	restart)
		echo "Restarting docker containers"
		for service in ${container_list}
		do
				docker-compose --file "${path_docker}/${service}/${service}.yml" restart
		done
		;;
	up)
		echo "Starting docker containers"
		for service in ${container_list}
		do
				docker-compose --file "${path_docker}/${service}/${service}.yml" up --detach
		done
		;;
	update)
		echo "Updating docker containers"
		for service in ${container_list}
		do
				docker-compose --file "${path_docker}/${service}/${service}.yml" down
				docker-compose --file "${path_docker}/${service}/${service}.yml" pull
				docker-compose --file "${path_docker}/${service}/${service}.yml" up --detach
		done
		;;
	*)
		echo "Not a valid argument, please use down, pull, restart, up or update!"
		exit 1
esac
