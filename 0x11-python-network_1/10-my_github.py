#!/usr/bin/python3

""" This module fetches using urllib """


from sys import argv
import requests

if __name__ == "__main__":
    # Get the commands line args
    user = argv[1]
    token = argv[2]
    url = f"https://api.github.com/users/{user}"
    req = requests.get(url, auth=(user, token))
    res_json = req.json()
    if 'id' in res_json:
        print(res_json['id'])
    
