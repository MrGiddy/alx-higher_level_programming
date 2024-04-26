#!/usr/bin/python3
"""Defines a function fetching a url"""
import urllib.request


def main(url):
    """Fetches a url"""
    req = urllib.request.Request(url)
    with urllib.request.urlopen(req) as response:
        cont = response.read()

    print("Body response:")
    print('\t- type:', type(cont))
    print('\t- content:', cont)
    print('\t- utf8 content:', cont.decode('utf-8'))


if __name__ == '__main__':
    main('https://alx-intranet.hbtn.io/status')
