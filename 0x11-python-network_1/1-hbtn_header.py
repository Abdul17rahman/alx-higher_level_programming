#!/usr/bin/python3

""" This module fetches using urllib """


import sys
import urllib.request

if __name__ == "__main__":
    with urllib.request.urlopen(sys.argv[1]) as res:
        # Retrieve the X-request-Id
        head = res.headers
        print(head.get('X-Request-Id'))
