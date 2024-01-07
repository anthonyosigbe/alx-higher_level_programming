#!/usr/bin/python3
"""Receives a URL, sends a request to that URL,
and then displays the response body (decoded in utf-8).

It also manages HTTPError exceptions to print
the HTTP Status Code if an error occurs.
"""

from sys import argv
from urllib.request import Request, urlopen
from urllib.parse import urlencode
from urllib.error import HTTPError


if __name__ == "__main__":
    req = Request(argv[1])

    try:
        with urlopen(req) as res:
            print(res.read().decode('utf-8'))
    except HTTPError as ex:
        print('Error code:', ex.code)
