#!/usr/bin/python3
if __name__ == "__main__":

import sys

addme = len(sys.argv)
res = 0

for nom in range(addme - 1):
    res += int(sys.argv[nom + 1])

print("{}".format(res))
