#!/usr/bin/python3

""" This module fetches using requests """


import sys
import requests
from requests.exceptions import HTTPError

if __name__ == "__main__":
    # Get the commands line args
    url = sys.argv[1]
    try:
        page = requests.get(url)
        page.raise_for_status()
        print(page.text)
    except HTTPError as e:
        print('Error code:', e.response.status_code)
