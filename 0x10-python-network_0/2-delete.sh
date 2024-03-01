#!/bin/bash
#sends DELETE request to URL passed as the 1st arg & displays the body of the response
curl -s -X DELETE "$1"
