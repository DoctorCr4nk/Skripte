#!/bin/bash


path_file_html_out='output.html'
url_chefkoch_base='https://www.chefkoch.de'
#url_chefkoch_sammlungen="${url_chefkoch_base}"'/mein-kochbuch/'
url_chefkoch_login="${url_chefkoch_base}"'/benutzer/einloggen?context=login/init'

path_file_credentials=".credentials.json"

username=$(jq '.username' "${path_file_credentials}")
password=$(jq '.password' "${path_file_credentials}")

echo "Username: ${username}"
echo "Password: ${password}"

curl --user "${username}":"${password}" "${url_chefkoch_login}" > ${path_file_html_out}