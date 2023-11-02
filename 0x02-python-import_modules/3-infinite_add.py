#!/usr/bin/python3

import sys

addme = sys.argv[1:]
sum_result = 0

for arg in addme:
    sum_result += int(arg)

print(sum_result)
