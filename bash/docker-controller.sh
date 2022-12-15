#!/bin/bash
## Author:       Alexander Mueller
## Email:        amueller@doctorcrank.de
## Version:      1.1
## Date:         2022-12-16
## Description:  Controll your docker containers

path_docker="/home/amueller/Docker"
#container_list="changedetection gitea grafana heimdall mailserver qbittorrent redmine nginx-proxy-manager smokeping unifi-controller wikijs"
container_list="gitea grafana heimdall redmine"

case ${1} in
	down)
		echo "Stopping docker containers"
		for service in ${container_list}
		do
				docker-compose --file "${path_docker}/${service}/${service}.yml" down
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
		echo "Not a valid argument, please use down, restart, up or update!"
		exit 1
esac
