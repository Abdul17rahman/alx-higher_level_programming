#!/usr/bin/python3

""" This module fetches using urllib """


import sys
import requests

if __name__ == "__main__":
    # Get the commands line args
    url = sys.argv[1]
    email = sys.argv[2]
    payload = {'email': email}
    # Retrieve the response
    page = requests.post(url, data=payload)
    print(page.text)
