#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    result = []
    for i in range(list_lenght):
        try:
            divison = 0
            if i < len(my_list_1) and i < len(my_list_2):
                divison = my_list_1[i] / my_list_2[i]
            else:
                raise IndexError("out of range")
            except (ZeroDivisonError, TypeError) as e:
                print("{}".format(e))
            finally:
                result.append(divison)
    return result
