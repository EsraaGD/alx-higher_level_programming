#!/bin/bash
#takes a URL, sends a request to that URL, displays the size of body of the response
curl -sI "$1" | grep -i Content-Length | awk '{print $2}'
