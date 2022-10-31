#!.venv-git_good_food/bin/python3.10
## Author:       Alexander Mueller
## Email:        amueller@doctorcrank.de
## Version:      1.0
## Date:         2022-10-30
## Comment:      Not working
## Description:  Try to generate a food plan for the upcoming week, using your chefkoch.de
##               cookbooks and offers at the supermarket

import json
import sys
import requests
import urllib.request
from bs4 import BeautifulSoup


path_file_credentials = '.credentials.json'
path_file_html_out = 'output.html'
url_chefkoch_base = 'https://www.chefkoch.de'
url_chefkoch_sammlungen = url_chefkoch_base + '/mein-kochbuch/'
url_chefkoch_login = url_chefkoch_base + '/benutzer/einloggen?context=login/init'
url_chefkoch_auth = url_chefkoch_base + '/benutzer/authentifizieren'

credentials = json.load(open(path_file_credentials))
credentials_dict = dict(username=credentials['username'], password=credentials['password'])
cred_chefkoch_username = credentials['username']
cred_chefkoch_password = credentials['password']

def chefkoch_login(mail, password):
    s = requests.Session()
    payload = {
#        '_token': 'F57hpKX33itHkrYIQk1uvGz97VqYfcEeBI7YtBsIp_I',
        'context': 'login/init',
        'ref': 'https://www.chefkoch.de/',
        'username': mail,
        'password': password,
        '_target_path': 'https://www.chefkoch.de/'
    }
    res = s.post(url_chefkoch_auth, data=payload)
    file = open(path_file_html_out, 'w')
    file.write(str(res.content))
    #print(type(res.content))
    return s

session = chefkoch_login(cred_chefkoch_username, cred_chefkoch_password)

