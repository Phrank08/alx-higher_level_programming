#!/usr/bin/python3

""" A function that adds all unique integers in a list"""
def uniq_add(my_list=[]):
    uniqueNumbers = set(my_list)
    SumOfUniqueNumbers = sum(uniqueNumbers)

    return SumOfUniqueNumbers
