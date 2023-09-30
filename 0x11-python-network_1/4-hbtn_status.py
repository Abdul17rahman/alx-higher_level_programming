#!/usr/bin/python3

""" This module fetches using urllib """


import requests

if __name__ == "__main__":
    body = requests.get('https://alx-intranet.hbtn.io/status')

print('Body response:')
print('\t- type:', type(body.text))
print('\t- content:', body.text)
