"""Bubble Sort: Is a sorting algorithm in python. with every pass the larger item is move to end.
It takes the n value it will compare from n+1 value, if n > n+1, it will swap the values."""


def bubble_sort1(li):
    # iterating through list
    for i in range(len(li)):
        # starting iteration from i + 1
        for j in range(i + 1, len(li)):
            # checking i value is greater than j value
            if li[i] > li[j]:
                # if above condition met, swapping the values
                li[i], li[j] = li[j], li[i]
    # It will make the changes inside the list
    # returning the list
    return li


def bubble_sort2(li):
    # Instead of 2 loops taking 1 loop
    # Iterating through the list to len(list) -1
    for i in range(len(li) - 1):
        # checking if i > i + 1 value
        if li[i] > li[i + 1]:
            # if above condition met, swapping the values
            li[i], li[i + 1] = li[i + 1], li[i]
    # It will make the changes inside the list
    # returning the list
    return li


arr = [8, 9, 5, 9, 8, 4, 8, 8, 4, 5]
print('Bubble sort with 2 loops', bubble_sort1(arr))
print('Bubble sort with 1 loop', bubble_sort2(arr))
