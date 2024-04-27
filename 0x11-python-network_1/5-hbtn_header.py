#!/usr/bin/python3
"""Defines a script that displays the value of a header variable"""
import requests


def main(url):
    """Sends a GET request and displays the value of a header variable"""
    req = requests.get(url)
    print(req.headers['X-Request-Id'])


if __name__ == '__main__':
    import sys
    url = sys.argv[1]
    main(url)
