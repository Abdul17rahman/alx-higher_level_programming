#!/usr/bin/python3

""" This module fetches using requests """


import sys
import requests

if __name__ == "__main__":
    # Get the commands line args
    q = sys.argv[1] if len(sys.argv) > 1 else ""
    payload = {'q': q}
    # Retrieve the response
    res = requests.post('http://0.0.0.0:5000/search_user', data=payload)
    # check if response is valid json
    try:
        res_json = res.json()
        if res_json:
            print("[{}] {}".format(res_json['id'], res_json['name']))
        else:
            print('No result')
    except ValueError:
        print('Not a valid JSON')
