#!/usr/bin/python3
"""Receives a URL, sends a request to it,
and shows the value of the `X-Request-Id`
variable found in the response header.
"""

from sys import argv
from urllib.request import Request, urlopen


if __name__ == "__main__":
    req = Request(argv[1])

    with urlopen(req) as res:
        headers = res.info()
        print(headers.get('X-Request-Id'))
