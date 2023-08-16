"""Now that you have learnt how to perform Binary Search, let us try
writing code for another edge case. Suppose your sorted array has
duplicate numbers.
For example, if the array is as follows: [1, 2, 2, 3, 3, 3, 4, 8, 9, 19, 19, 19]
Try writing the code for the following two cases.
1. Finding first occurrence of the given number.
2. Finding the last occurrence of the given number"""


def find_element(li, ele):
    try:
        fist_occ = -4546
        last_occ = -5656
        low = 0
        high = len(li) - 1
        while low <= high:
            mid = (low + high) // 2
            if li[mid] == ele:
                if last_occ < 0:
                    last_occ = mid
                else:
                    fist_occ = mid
                li.pop(mid)
            elif arr[mid] > ele:
                high = mid - 1
            else:
                low = mid + 1
        if last_occ < 0:
            return "No element found in {}".format(li)
        print('First occurrence at index {}'.format(last_occ))
        if fist_occ < 0:
            return "Last occurrence is not found in {}".format(li)
        print('Last Occurrence at index {}'.format(fist_occ))
    except Exception as e:
        return e


arr = [1, 2, 2, 3, 3, 3, 4, 8, 9, 19, 19, 19]

ele1 = 3
ele2 = 1
ele3 = 100
print(find_element(arr, ele1))
print(find_element(arr, ele2))
print(find_element(arr, ele3))
