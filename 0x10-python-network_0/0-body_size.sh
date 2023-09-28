#!/bin/bash
# Script to display the size of the body
curl -s "$1" | wc -c
