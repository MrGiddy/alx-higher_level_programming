#!/usr/bin/python3
"""Defines a script that sends a get request and displays the response"""
import requests


def main(url):
    """Sends a get request and displays the response body"""
    req = requests.get(url)
    if req.status_code >= 400:
        print("Error code:", req.status_code)
        return
    print(req.text)


if __name__ == '__main__':
    import sys
    url = sys.argv[1]
    main(url)
