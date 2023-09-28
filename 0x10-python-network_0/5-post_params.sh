#!/bin/bash
# Make a post request with parameters
curl -sX POST -F "email=test@gmail.com&subject=I will always be here for PLD" -F "$1"
