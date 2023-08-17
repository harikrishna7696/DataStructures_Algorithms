"""Insertion Sort: It is also a straight forward algorith used to sort. The algorithm initially it take 2 list one is
sorted and another unsorted ex: [1,5,5,6,8,4,5] [1] -> Sorted, unsorted -> [5,5,6,8,4,5], 0 index is sorted array
It will loop through the unsorted it will access one element, it will compare with sorted array, if any value in sorted
array is greater than it will shift the position."""


def insertion_sort(arr):
    # looping from 1 index, 0 is sorted array
    for i in range(1, len(arr)):
        # access the sorted array value
        j = i - 1
        # storing the value of unsorted array
        temp = arr[i]
        # if j >= 0 and value need to greater than temp value
        while j >= 0 and arr[j] > temp:
            # if condition met, it will assign the value to index
            arr[j + 1] = arr[j]
            # decrementing the value
            j -= 1
        # if j  0 or value is < than temp value
        # in that jth position will assign temp value, which means we are find the desire position
        arr[j + 1] = temp
    return arr


li = [8, 9, 45, 4, 89, 8]
print(insertion_sort(li))
