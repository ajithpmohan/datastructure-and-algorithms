def hash(a_string, table_size):
  sum = 0
  for pos in range(len(a_string)):
    sum = sum + (ord(a_string[pos])*(pos+1))
  return sum % table_size


print hash('cat',11)
