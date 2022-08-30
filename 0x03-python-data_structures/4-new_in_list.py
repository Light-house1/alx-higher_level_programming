#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    new_my_list = my_list.copy()
    if 0 <= idx < len(my_list):
         new_my_list[idx] = element
         return new_my_list
    else:
        return my_list
    return my_list
