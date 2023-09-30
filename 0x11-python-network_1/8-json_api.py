#!/usr/bin/python3

""" This module fetches using requests """


import sys
import requests

if __name__ == "__main__":
    # Get the commands line args
    q = sys.argv[1] if len(sys.argv) > 1 else ""
    payload = {'q': q}
    # Retrieve the response
    res = requests.post('http://0.0.0.0:5000/search_user', data=payload).json()
    # check if response is valid json
    # if res.status_code == 200:
    # res_json = res.json()
    if isinstance(res, dict):
        if res:
            print("[{}] {}".format(res['id'], res['name']))
        else:
            print('No result')
    else:
        print('Not a valid JSON')
