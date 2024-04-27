#!/usr/bin/python3
"""Defines a script that displays the body of a response"""
import urllib.request
import urllib.parse


def main(url, email):
    """Sends a POST request and displays response body"""
    post_data = urllib.parse.urlencode({'email': email})
    post_data = post_data.encode('ascii')
    req = urllib.request.Request(url, data=post_data, method='POST')
    with urllib.request.urlopen(req) as response:
        print(response.read().decode('utf-8'))


if __name__ == '__main__':
    import sys
    url, email = sys.argv[1:]
    main(url, email)
