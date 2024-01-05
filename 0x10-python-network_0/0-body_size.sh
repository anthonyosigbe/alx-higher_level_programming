#!/bin/bash
# Retrieve the byte size of the HTTP response header for a specified URL.
curl -s "$1" | wc -c
