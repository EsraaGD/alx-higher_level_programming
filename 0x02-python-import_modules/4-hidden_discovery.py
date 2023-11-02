#!/usr/bin/python3
if __name__ == "__main__":
    import hidden_4
    names = dir(hidden_4)
    for y in names:
        if "__" not in y:
            print(y)
