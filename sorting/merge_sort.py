"""Merge sort is a very efficient sorting algorithm. It’s based on the divide-and-conquer approach,
a powerful algorithmic technique used to solve complex problems."""


def merge_sort(arr1, arr2):
    i, j = 0, 0
    new_array = []
    len_1, len_2 = len(arr1), len(arr2)

    while i < len_1 and j < len_2:
        if arr1[i] < arr2[j]:
            new_array.append(arr1[i])
            i += 1
        else:
            new_array.append(arr2[j])
            j += 1
    while i < len_1:
        new_array.append(arr1[i])
        i += 1
    while j < len_2:
        new_array.append(arr2[j])
        j += 1
    return new_array


a1 = [1, 3, 4, 7, 11, 15]
a2 = [2, 4, 6, 13, 14]
print(merge_sort(a1, a2))