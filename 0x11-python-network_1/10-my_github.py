#!/usr/bin/python3

""" This module fetches using urllib """


from sys import argv
import requests
from requests.auth import HTTPBasicAuth

if __name__ == "__main__":
    # Get the commands line args
    user = argv[1]
    token = argv[2]
    git_auth = HTTPBasicAuth(user, token)
    url = "https://api.github.com/user"
    req = requests.get(url, auth=git_auth)
    res_json = req.json()
    print(res_json.get('id'))
