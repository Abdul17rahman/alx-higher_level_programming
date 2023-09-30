#!/usr/bin/python3

""" This module fetches using urllib """


from sys import argv
import requests

if __name__ == "__main__":
    url = f'https://api.github.com/repos/{argv[2]}/{argv[1]}/commits'
    r = requests.get(url)
    for commit in r.json()[:10]:
        try:
            print(f"{commit.get('sha')}: "
                  f"{commit.get('commit').get('author').get('name')}")
        except IndexError:
            break
