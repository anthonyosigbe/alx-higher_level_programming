#!/bin/bash
# Bash scripts that send a POST request to a specified URL.
curl -s "$1" -X POST -d "email=test@gmail.com&subject=I will always be here for PLD"
