#!/bin/bash
# Author:       Alexander Mueller
# Email:        amueller@doctorcrank.de
# Version:      1
# Date:         2022-07-21
# Comment:      
# Description:  This script will generate a new script based on this template

author=$(git config --list | grep "user.name" | cut --delimiter "=" --fields "2")
email=$(git config --list | grep "user.email" | cut --delimiter "=" --fields "2")
version="1"
date=$(date +%Y-%m-%d)
comment="Wow is this a cool script generator"
description="Check out my other scripts at https://github.com/DoctorCr4nk"
path_file_script="${1}"
arg_quiet=""
arg_verbose=""

usage ()
{
    echo -e "${0} [ARGUMENTS] -f <scriptname>"
    echo -e ""
    echo -e ""
}

if [ -z "${1}" ]
then
    echo "Please provide a script name."
    exit 1
fi

while getopts "f:h" argument
do
    case "${argument}" in
        f)
            script_name="${OPTARG}"
            ;;
        h)
            usage
            exit 0
            ;;
        *)
        echo "foo"
        ;;
    esac
done

echo "${script_name} will be generated!"

exit 2

echo '#!/bin/bash'                      | tee "${path_file_script}"
echo '# Author:       '"${author}"      | tee --append "${path_file_script}"
echo '# Email:        '"${email}"       | tee --append "${path_file_script}"
echo '# Version:      '"${version}"     | tee --append "${path_file_script}"
echo '# Date:         '"${date}"        | tee --append "${path_file_script}"
echo '# Comment:      '"${comment}"     | tee --append "${path_file_script}"
echo '# Description:  '"${description}" | tee --append "${path_file_script}"

echo "${path_file_script} was created"