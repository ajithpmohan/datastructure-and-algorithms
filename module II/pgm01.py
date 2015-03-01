#Devise an experiment to verify that the list index operator is O(1).

li=range(10,100,10)
import timeit
from timeit import Timer
time_one=Timer('li.index(20)','from __main__ import li')
time_two=Timer('li.index(90)','from __main__ import li')
print time_one.timeit(number=1000)
print time_two.timeit(number=1000)

