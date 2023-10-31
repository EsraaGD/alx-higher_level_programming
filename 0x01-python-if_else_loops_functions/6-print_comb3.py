#!/usr/bin/python3

for f1 in range(10):
    for f2 in range(f1 + 1, 10):
        if f1 == 8 and f2 == 9:
            print("{}{}".format(f1, f2))
        else:
            print("{}{}, ".format(f1, f2), end="")
