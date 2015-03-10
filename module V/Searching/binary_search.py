def binary_search(lists, item):
  first = 0
  last  = len(lists)-1
  found = False
  while first <= last and not found:
    midpoint = (first+last) / 2
    if lists[midpoint]  == item:
      found=True
    elif item < lists[midpoint]:
      last = midpoint - 1
    else:
      first=midpoint + 1
  return found


lists = range(10,1000,37)
print binary_search(lists,491)
print binary_search(lists,840)
