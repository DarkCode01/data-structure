def binary_search(arr, x, m, mx):
  middle = (mx + m) // 2

  if x > arr[middle]:
    return binary_search(arr, x, middle + 1, mx)
  elif x < arr[middle]:
    return binary_search(arr, x, m, middle - 1)
  else:
    return middle

l = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(binary_search(l, 3, 0, 9))
