#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    if my_list is not None:
        i = 0
        NewList = []
        for element in my_list:
            if my_list[i] % 2 == 0:
                NewList.append(True)
            else:
                new_list.append(False)
            i = i + 1
        return NewList
