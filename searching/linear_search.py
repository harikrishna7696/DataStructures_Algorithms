""" Linear Search: Is a method in python to find an element in the list. We go through with every element in list or tuple
or set, if element matches with required element that we are seeking, will return index else return -1"""
import array
import numpy as np


# creating the function it will take the list and element that we need to find.
def linear_search(li, element):
    try:
        # finding the type of data type
        type_li = type(li)
        # if any iterable data type found ex: list, tuple, set .
        if type_li is list or type_li is tuple or type_li is set or type_li is array or type_li is np.array:
            # Iterating through list
            for index in range(len(li)):
                # accessing the element with index
                # checking the element is matching or not
                if li[index] == element:
                    # if element found returning the index of element
                    return "Element found at index {}.".format(index)
            # If element not found returning the message below
            return "No element found with {}.".format(element)
        # If data type is not satisfied returning the error.
        return "Please check the {} is not iterable.".format(li)
    except Exception as e:
        print(e)


li1 = [5, 6, 8, 7, 9]
ele = 7
ele1 = 10
print(linear_search(li1, ele))
print(linear_search(li1, ele1))
