#!/usr/bin/python3
"""Defines a script that displays the body of a http response"""
import urllib.request
import urllib.error


def main(url):
    """Displays the body of a http response"""
    try:
        req = urllib.request.Request(url)
        with urllib.request.urlopen(req) as response:
            cont = response.read()
        print(cont.decode('utf-8'))
    except urllib.error.HTTPError as e:
        print("Error code:", e.code)


if __name__ == '__main__':
    import sys
    url = sys.argv[1]
    main(url)
