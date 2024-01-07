#!/usr/bin/python3
"""
Display the 10 most recent commits
(from the most recent to the oldest)
of a repository by a specific user.

This script utilizes the GitHub API
to retrieve and print all commits
in the format `<sha>: <author name>`
(one per line) for a specific user.
"""

from sys import argv
import requests


if __name__ == "__main__":
    url = 'https://api.github.com'
    uri = '{0}/repos/{1}/{2}/commits'.format(url, argv[2], argv[1])
    req = requests.get(uri).json()

    for com in req[0:10]:
        print(com['sha'] + ':', com['commit']['author']['name'])
