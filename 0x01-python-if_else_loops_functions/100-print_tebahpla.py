#!/usr/bin/python3
for r in range(26):
    if r % 2 == 0:
        print('{:c}'.format(122 - r), end='')
    else:
        print('{:c}'.format(90 - r), end='')
