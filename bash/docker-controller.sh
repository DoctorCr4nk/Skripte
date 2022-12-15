#!/bin/bash
## Author:       Alexander Mueller
## Email:        amueller@doctorcrank.de
## Version:      1.0
## Date:         2022-12-16
## Description:  Controll your docker containers

path_docker="/home/amueller/Docker"
#service_list="changedetection gitea grafana heimdall mailserver qbittorrent redmine nginx-proxy-manager smokeping unifi-controller wikijs"
service_list="gitea grafana heimdall redmine"

if [[ ${1} == "up" ]]
then
	echo "Start docker container"
	for service in ${service_list}
	do
        	docker-compose --file "${path_docker}/${service}/${service}.yml" up --detach
	done
elif [[ ${1} == "down" ]]
then
	echo "Stop docker container"
	for service in ${service_list}
	do
        	docker-compose --file "${path_docker}/${service}/${service}.yml" down
	done
else
	echo "Wrong argument, only up or down accepted"
	exit 1
fi
