#!/usr/bin/python3
"""Defines a script that sends a POST request with a letter paramter"""
import requests


def main(url, letter):
    """Sends a POST request with a letter as a paramter"""
    payload = {"q": letter}

    req = requests.post(url, data=payload)
    try:
        resp = req.json()
        if resp == {}:
            print("No result")
        else:
            print(f'[{resp.get("id")}] {resp.get("name")}')
    except ValueError:
        print('Not a valid JSON')


if __name__ == '__main__':
    import sys
    if len(sys.argv) == 1:
        letter = ""
    else:
        letter = sys.argv[1]
    url = 'http://0.0.0.0:5000/search_user'
    main(url, letter)
