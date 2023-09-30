#!/bin/bash
# URL as argument and display the code
curl -s -o /dev/null -w "%{http_code}" "$1"
