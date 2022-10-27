#!/bin/bash

path_dir_videos="/mnt/share/Videos"
path_dir_youtube="${path_dir_videos}/Youtube"
path_dir_twitch="${path_dir_videos}/TwitchVODs"
path_file_csv="${path_dir_videos}/fsize.csv"

echo -e "Filesize;Videolength;Rate" | tee "${path_file_csv}"
for video in "${path_dir_twitch}"/*/*.mp4
do
    fsize=$(du -b "${video}" | awk '{print $1}')
    vlength=$(ffprobe  -show_entries format=duration -v quiet -of csv="p=0" -i "${video}" | cut -d'.' -f1)
    rate=$((fsize/vlength))
    echo -en "${fsize};${vlength};${rate}\n" | tee --append "${path_file_csv}"
done
