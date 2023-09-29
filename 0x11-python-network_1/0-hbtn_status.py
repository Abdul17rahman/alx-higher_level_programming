#!/usr/bin/python3

""" This module fetches using urllib """


import urllib.request

with urllib.request.urlopen('https://alx-intranet.hbtn.io/status') as res:
    body = res.read()
    content = body.decode('utf-8')

print('Body response:')
print('\t- type:', type(body))
print('\t- content:', body)
print('\t- utf8 content:', content)
