#!/usr/bin/python3

""" This module fetches using urllib """


from sys import argv
import requests

if __name__ == "__main__":
    # Get the commands line args
    user = argv[1]
    repo = argv[2]
    url = f"https://api.github.com/repos/{user}/{repo}/commits"
    req = requests.get(url)
    res_json = req.json()[:10]
    """
    for commit in res_json:
        try:
            print("{}: {}".format(commit.get('sha'),
                  commit.get('commit').get('author').get('name')))
        except KeyError:
            pass
    """
    print(res_json[0].get('commit'))
