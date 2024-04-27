#!/usr/bin/python3
"""Defines a script that sends a POST request and displays response"""
import requests


def main(url, email):
    """Sends a POST request and displays the response body"""
    payload = {'email': email}
    req = requests.post(url, data=payload)
    print(req.text)


if __name__ == '__main__':
    import sys
    url, email = sys.argv[1:]
    main(url, email)
