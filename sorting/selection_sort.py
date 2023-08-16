""" Selection Sort: Is a sorting algorithm, that use to sort the array. Initially, it start assuming the 0 index is
minimum value while iterating over the list, will update the minimum index after one complete iteration we get minimum
we just swap the value after completing all iterations we get sorted array """


def selection_sort(arr):
    # Iterating through the list
    for i in range(len(arr) - 1):
        # Initial we assume the current value is the minimum value
        min_index = i
        # Initiating another iterations from i + 1 index
        for j in range(i + 1, len(arr)):
            # will check if the j value is less than the minimum value
            if arr[j] < arr[min_index]:
                # if j is less than min_index value, we update the index
                min_index = j
        # After every iteration we get the minimum value index, we just swap the values.
        arr[i], arr[min_index] = arr[min_index], arr[i]
    return arr


arr1 = [8, 9, 8, 6, 4, 9, 4, 5, 8]
arr2 = [54, 89, 54, 9, 5, 9, 5, 9, 5, 65, 2652, 652]

print(selection_sort(arr1))
print(selection_sort(arr2))
