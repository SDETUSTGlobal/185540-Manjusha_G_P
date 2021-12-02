# def adder(x, y)
# return x+y
# print(adder(1, 2))
# Example 1
adder = lambda x, y: x + y
print(adder(1, 2))
# Example 2
sting = 'some kind of a useless lambda'
(lambda sting : print(sting))(sting)
# Example 3
m = 10
n = 20
(lambda m, n: print(m * n))(m,n)

#lambdas in filter()
sequences = [10,2,8,7,5,4,3,11,0, 1]
filtered_result = filter (lambda x: x > 4, sequences)
print(list(filtered_result))

#lambdas in map()
sequences = [10,2,8,7,5,4,3,11,0, 1]
filtered_result = map (lambda x: x*x, sequences)
print(list(filtered_result))

#lambdas in reduce()
from functools import reduce
sequences = [1,2,3,4,5]
product = reduce (lambda x, y: x*y, sequences)
print(product)
