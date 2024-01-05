#!/bin/bash
# This program sends a request to a specified URL and then displays only the response's status code.
curl -s -o /dev/null -w '%{http_code}' "$1"
