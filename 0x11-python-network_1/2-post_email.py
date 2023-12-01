#!/usr/bin/python3

""" This module fetches using urllib """


import sys
import urllib.request
import urllib.parse

if __name__ == "__main__":
    # Get the commands line args
    url = sys.argv[1]
    email = sys.argv[2]
    params = {'email': email}
    data = urllib.parse.urlencode(params)
    data = data.encode('ascii')
    req = urllib.request.Request(url, data)
    with urllib.request.urlopen(req) as res:
        # Retrieve the response
        page = res.read().decode('utf-8')
        print(page)
