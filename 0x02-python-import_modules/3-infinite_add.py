#!/usr/bin/python3
if __name__ == "__main__":

import sys

addme = sys.argv[1:]
res = 0

for nom in addme:
    res += int(nom)

print("{}".format(res))
