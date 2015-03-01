#Devise an experiment to verify that get item and set item are O(1) for dictionaries.

dic={'a':1,'b':2,'c':3,'d':4}

import timeit
from timeit import Timer

time_one=Timer('dic.__getitem__("a")','from __main__ import dic')
time_two=Timer('dic.__getitem__("b")','from __main__ import dic')
time_three=Timer('dic.__setitem__("e",5)','from __main__ import dic')
time_four=Timer('dic.__setitem__("f",6)','from __main__ import dic')

print time_one.timeit(number=1000)
print time_two.timeit(number=1000)
print time_three.timeit(number=1000)
print time_four.timeit(number=1000)
