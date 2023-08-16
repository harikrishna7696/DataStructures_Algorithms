""" Binary Search: Is a method in python, It finds the given element in the array or any iterable datatypes.
Binary Search is an efficient algorithm compare to linear search, Binary Search follow divide and conquer method. It
will only work with sorted array, you cannot apply this algorithm on unsorted array."""
import numpy as np
import array


def binary_search(arr, element):
    try:
        # finding the type of data type
        type_li = type(arr)
        # if any iterable data type found ex: list, tuple, set .
        if type_li is list or type_li is tuple or type_li is set or type_li is array or type_li is np.array:
            # taking low index 0, which is starting index of any iterate data type
            low = 0
            # taking the high index as len(iterable)-1 which is last index of list.
            high = len(arr)-1
            # checking the low index must be less than high index
            # because if both crossed it mean, the list is over
            while low <= high:
                # calculating the mid-index by dividing the low and high indexes
                mid = (low + high) // 2
                if arr[mid] == element:
                    # if mid-value matches the element. returning the index
                    return "Element found at index {}.".format(mid)
                # if mid-value is greater than element. we don't need right side list
                # because remaining right side list values is greater our required value
                elif arr[mid] > element:
                    # if value is > element, high index starts with mid-index -1
                    high = mid - 1
                else:
                    # if value is < element, low index starts with mid-index + 1
                    low = mid + 1
            return "Element is not found in {}.".format(arr)

        # If data type is not satisfied returning the error.
        return "Please check the {} is not iterable.".format(arr)
    except Exception as e:
        print(e)


li = [1, 2, 3, 4, 6]
ele1 = 10
ele2 = 2
ele3 = 6
print(binary_search(li, ele1))
print(binary_search(li, ele2))
print(binary_search(li, ele3))
