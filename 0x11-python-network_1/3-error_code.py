#!/usr/bin/python3

""" This module fetches using urllib """


import sys
import urllib.request
import urllib.parse
import urllib.error

if __name__ == "__main__":
    # Get the commands line args
    url = sys.argv[1]
    try:
        with urllib.request.urlopen(url) as res:
            # Retrieve the response
            page = res.read().decode('utf-8')
            print(page)
    except urllib.error.HTTPError as e:
        print('Error code:', e.code)
