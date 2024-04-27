#!/usr/bin/python3
"""Defines a script that uses GitHub API to display id"""
import requests
from requests.auth import HTTPBasicAuth


def main(username, password, url):
    """Uses GitHub API to display a User's id"""
    auth = HTTPBasicAuth(username, password)
    req = requests.get(url)
    print(req.json().get("id"))
    

if __name__ == '__main__':
    import sys
    username, password = sys.argv[1:]
    url = 'https://api.github.com/user'
    main(username, password, url)
