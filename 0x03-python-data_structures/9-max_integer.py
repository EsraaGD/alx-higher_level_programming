#!/usr/bin/python3
def max_integer(my_list=[]):
    if len(my_list) == 0:
        return("None")
    else:
        max = my_list[0]
        for number in range(len(my_list)):
            if my_list[number] > max:
                max = my_list[number]
        return max