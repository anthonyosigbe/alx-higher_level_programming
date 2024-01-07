#!/usr/bin/python3
"""
Receives a URL, sends a request to that URL,
and displays the body of the response
(decoded in utf-8) using the `requests` module.
"""

from sys import argv
import requests


if __name__ == "__main__":
    req = requests.get(argv[1])

    if req.status_code >= 400:
        print('Error code:', req.status_code)
    else:
        print(req.text)
