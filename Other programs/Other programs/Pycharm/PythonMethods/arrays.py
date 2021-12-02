import array

abc = array.array('d', [3, 9, 6, 5, 20, 13, 19, 22, 30, 25])
print("Array first element is:", abc[0])
print("Array last element is:", abc[-1])
print(abc[1:4])
print(abc[7:10])
# inserting elements into array
abc.insert(2, 150)  # (index no., element)
print(abc)
# replacing/modifying element
abc[0] = 999
print(abc)
# concatenation
first = array.array('b', [4, 6, 8])
second = array.array('b', [9, 12, 15])
numbers = first + second
print(numbers)
# pop()/remove element from array
second.pop(1)  # value at [1] is deleted from second
print(second)
# delete element from array
del first[0]  # value at [0] is deleted from second
print(first)
# remove element value
first.remove(8)  # 8 is removed from first
print(first)
# find the value in the array
print(abc.index(22))  # search value 22 in abc and give that element index
# reverse array
abc.reverse()
print(abc)
# count occurrence of a value
num = array.array('b', [2, 3, 5, 4, 3, 3, 3])
print(num.count(3))
# Traverse an Array
balance = array.array('i', [300, 200, 100])
for x in balance:
    print(x)
# unicode
from array import array
p = array('u', [u'\u0050', u'\u0059', u'\u0054', u'\u0048', u'\u004F', u'\u004E'])
print(p)
q = p.tounicode()
print(q)
