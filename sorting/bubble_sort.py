def bubble_sort1(li):
  for i in range(len(li)):
    for j in range(i+1, len(li)):
      if li[i] > li[j]:
        li[i], li[j] = li[j], li[i]
  return li


def bubble_sort2(li):
  for i in range(len(li)-1):
    if li[i] > li[i+1]:
      li[i], li[i+1] = li[i+1], li[i]
  return li


l = [8, 9, 5, 9, 8, 4, 8, 8, 4, 5]
print('Bubble sort with 2 loops', bubble_sort1(l))
print('Bubble sort with 1 loop', bubble_sort2(l))
