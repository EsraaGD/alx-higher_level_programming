#!/usr/bin/python3

if __name__ == "__main__":
    import sys

    noarg = len(sys.argv) - 1

    if noarg == 0:
        print("0 arguments.")

    elif noarg == 1:
        print("1 argument:")

    else:
        print("{} arguments:".format(noarg))

        for o in range(noarg):
            print("{}: {}".format(o + 1, sys.argv[o + 1]))
