#!/usr/bin/python3
"""Defines a script that uses GitHub API to display id"""
import sys
import requests
from requests.auth import HTTPBasicAuth


def main():
    """Uses GitHub API to display a User's id"""
    username, password = sys.argv[1:]
    gh_api = 'https://api.github.com/user'

    auth = HTTPBasicAuth(username, password)
    req = requests.get(gh_api, auth=auth)
    print(req.json().get("id"))


if __name__ == '__main__':
    main()
