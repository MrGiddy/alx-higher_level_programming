#!/usr/bin/python3
"""Defines a script using requests module to fetch a url"""
import requests


def main(url):
    """Sends a GET request and displays the body of the response"""
    req = requests.get(url)
    print('Body response:')
    print('\t- type:', type(req.text))
    print('\t- content:', req.text)


if __name__ == '__main__':
    url = 'https://alx-intranet.hbtn.io/status'
    main(url)
