#!/bin/bash
# Send a request to a json
curl -sLf "$1" -X POST -H "Content-Type: application/json" -d @"$2"
