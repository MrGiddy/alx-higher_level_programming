#!/usr/bin/python3
"""Defines a function that displays a response header value"""
import urllib.request


def main(url):
    """Displays the header value of a response"""
    req = urllib.request.Request(url)
    with urllib.request.urlopen(req) as response:
        pass
    print(response.getheader('X-Request-Id'))


if __name__ == '__main__':
    import sys
    main(sys.argv[1])
