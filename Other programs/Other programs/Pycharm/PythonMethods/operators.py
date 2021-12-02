x = 8
y = 6
# arithmetic
print("Sum is :", x + y)
print("Difference is :", x - y)
print("Product is :", x * y)
print("Quotient is :", x / y)
print(x // y)
# comparison
print(x > y)
print(x < y)
print(x == y)
print(x >= y)
print(x <= y)
print(x != y)
# assignment(=)
res = x + y  # 8+6=14
res += x  # res = res+x = 14+8 =22
print(res)
# logical
a = True
b = False
print(('a and b is', a and b))
print(('a or b is', a or b))
print(('not a is', not a))
# membership
m = 4
n = 8
list = [1, 2, 3, 4, 5];
if m in list:
    print("Line 1 - m is available in the given list")
else:
    print("Line 1 - m is not available in the given list")
if n not in list:
    print("Line 2 - n is not available in the given list")
else:
    print("Line 2 - n is available in the given list")
# identity
j = 20
k = 20
if j is k:
    print("j & k  SAME identity")
k = 30
if j is not k:
    print("j & k have DIFFERENT identity")
# Operator precedence
a1 = 4
a2 = 5
a3 = 8
a4 = 2
s = (a1+a2) * a3 / a4
print("Value of (a1+a2) * a3 / a4 is ",  s)
