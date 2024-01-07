#!/usr/bin/python3
"""
Accepts a URL and an email address as input,
sends a POST request to the provided URL
with the email as a parameter, and then
displays the body of the response.
"""

from sys import argv
import requests


if __name__ == "__main__":
    payload = {'email': argv[2]}
    req = requests.post(argv[1], data=payload)

    print(req.text)
