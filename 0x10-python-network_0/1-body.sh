#!/bin/bash
#takes in a URL, sends GET request to URL, and displays body of the response
curl -s -o response.txt -w "%{http_code}" "$1" | awk '/200/{flag=1} flag'
