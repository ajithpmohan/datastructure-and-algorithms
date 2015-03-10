def bubble_sort(a_list):
  for pass_num in range(len(a_list) - 1, 0, -1):
    for i in range(pass_num):
      if a_list[i] > a_list[i + 1]:
        a_list[i], a_list[i + 1] = a_list[i + 1], a_list[i]
    
a_list = [54, 12, 87, 62, 26, 93, 17, 77, 31, 96, 44, 55, 03, 20]
bubble_sort(a_list)

print a_list
