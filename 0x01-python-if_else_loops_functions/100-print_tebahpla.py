#!/usr/bin/python3

for av in range(122, 96, -1):
    char = chr(av)
    case = "lower" if av % 2 == 0 else "upper"
    print("{}".format(char.upper() if case == 'lower' else char), end="")
