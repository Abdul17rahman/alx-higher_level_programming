#!/bin/bash
# Get methods
curl -sX OPTIONS "$1" -I | sed -n 's/Allow: //p'
