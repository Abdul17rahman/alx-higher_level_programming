#!/usr/bin/python3

""" This module fetches using urllib """


import sys
import requests

if __name__ == "__main__":
    url = sys.argv[1]
    # Retrieve the X-request-Id
    head = requests.Request(url)
    print(head.headers.get('X-Request-Id'))
