#!/bin/bash
#takes in a URL and displays all HTTP methods the server will accept
curl -s -I -X OPTIONS "$1" | grep -i allow | sed 's/Allow://' | tr -d '\r'

