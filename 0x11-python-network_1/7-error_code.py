#!/usr/bin/python3

""" This module fetches using urllib """


import sys
import requests

if __name__ == "__main__":
    # Get the commands line args
    url = sys.argv[1]
    try:
        page = requests.get(url)
        print(page.text)
    except HTTPError as e:
        print('Error code:', e.code)
