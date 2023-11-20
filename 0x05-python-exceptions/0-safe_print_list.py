#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    try:
        xx = 0
        for i in range(x):
            print("{}".format(my_list[i]), end="")
            xx += 1
        print()
        return xx
    except IndexError:
        print()
        return xx
