# print the values from 0-9
for i in range(10):
    print(i, end=" ")
print('\n')
# print the values from 3-9
for i in range(3, 10):
    print(i, end=" ")
print('\n')
# each value in the sequence will be incremented by 2
for i in range(3, 10, 2):
    print(i, end=" ")
print('\n')
# each value in the sequence will be incremented by 5
for i in range(1, 30, 5):
    print(i, end=" ")
print('\n')
# Decrementing the values
for i in range(5, -2, -1):
    print(i, end =" ")
print('\n')
# array of numbers
arr_list = ['Mysql', 'Mongodb', 'PostgreSQL', 'Firebase']
for i in range(len(arr_list)):
    print(arr_list[i], end =" ")
print('\n')
# range as a list
print(list(range(10)))
print('\n')
# list of the alphabets
def get_alphabets(startletter, stopletter, step):
    for c in range(ord(startletter.lower()), ord(stopletter.lower()), step):
        yield chr(c)
print(list(get_alphabets("a", "z", 1)))
print('\n')
# use the index to access the elements from range()
for i in range(6):
    print(i)
startvalue = range(5)[0]
print("The first element in range is = ", startvalue)

secondvalue = range(5)[1]
print("The second element in range is = ", secondvalue)

lastvalue = range(5)[-1]
print("The first element in range is = ", lastvalue)
# Merging two-range() outputs
from itertools import chain

print("Merging two range into one")
frange =chain(range(10), range(10, 20, 1))
for i in frange:
    print(i, end=" ")
print('\n')
# range() using NumPy
import numpy as np
for  i in np.arange(10):
   print(i, end =" ")
print('\n')
# Floating point numbers using NumPy arange()
for  i in np.arange(0.5, 1.5, 0.2):
   print(i, end =" ")
