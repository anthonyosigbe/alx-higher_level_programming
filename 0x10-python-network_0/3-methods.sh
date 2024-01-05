#!/bin/bash
# Show all the HTTP methods that the server of a given URL will accept.
curl -sI "$1" -X OPTIONS | grep "Allow:" | cut -d':' -f2 | sed 's/ //'
