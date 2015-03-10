def binary_search(lists, item):
  if len(lists) == 0:
    return False
  else:
    midpoint = len(lists) // 2
    if lists[midpoint] == item:
      return True
    elif item < lists[midpoint]:
      return binary_search(lists[:midpoint], item)
    else:
      return binary_search(lists[midpoint + 1:], item)

lists = [0, 1, 2, 8, 13, 17, 19, 32, 42,]
print binary_search(lists, 3)
print binary_search(lists, 19)
