#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    xx = 0
    for i in range(x):
        try:
            print("{:d}".format(my_list[i]), end="")
            xx += 1
        except (TypeError, IndexError):
            pass
    print()
    return xx
