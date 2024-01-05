#!/bin/bash
# Sends a DELETE request to the specified URL in the first argument and shows the response body.
curl -s "$1" -X DELETE
