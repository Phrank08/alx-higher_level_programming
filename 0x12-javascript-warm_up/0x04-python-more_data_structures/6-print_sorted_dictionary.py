#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    sortedDictionary = sorted(a_dictionary)

    for keys in sortedDictionary:
        print(f"{keys}: {sortedDictionary}")
    return sortedDictionary
