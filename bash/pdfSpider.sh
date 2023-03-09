#!/bin/bash
## Author:       Alexander Mueller
## Email:        amueller@doctorcrank.de
## Version:      1.0
## Date:         2022-02-24
## Comment:      NOT usable before modification
## Description:  Downloads PDF files from a certain website.

## Check for trailing slash and remove it
removeTrailingSlash ()
{
    if [ "${1: -1}" == '/' ]
    then
        echo "${1%?}"
    else
        echo "${1}"
    fi
}

if [ -z "${1}" ]
then
    echo "Please provide a base URL."
    exit
fi

dir_save=${PWD}/$(date +%Y-%m-%d-download)
if [ ! -d "${dir_save}" ]
then
    mkdir "${dir_save}" || exit
fi

echo "PDFs will be saved to ${dir_save}"

url_base=$(removeTrailingSlash "${1}")
url_list=$(curl -s "${url_base}/" | grep "^<p" | grep href | grep -v privacy | cut -d'"' -f6 | sed 's# #%20#g')

for url_sub in ${url_list}
do
    url_sub_wo_index=$(removeTrailingSlash "${url_sub//index.html//}")
    url_sub_list=$(curl -s "${url_base}/${url_sub}" | grep "^  <a href=" | cut -d'"' -f2 | sed 's# #%20#g')
    for url_pdf in ${url_sub_list}
    do
        pdf_name=$(echo "$url_pdf" | sed 's#%20##g' )
        wget "${url_base}/${url_sub_wo_index}${url_pdf}" -O "${dir_save}/${pdf_name}" -o ->> "${dir_save}/wget.log"
    done
done
