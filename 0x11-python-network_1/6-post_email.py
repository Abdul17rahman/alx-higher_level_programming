#!/usr/bin/python3

""" This module fetches using urllib """


import requests

with urllib.request.urlopen(sys.argv[1]) as res:
    head = res.headers
    print(head['X-Request-Id'])
