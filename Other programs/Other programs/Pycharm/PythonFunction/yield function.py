# Example1
def testyield():
  yield "Welcome to Guru99 Python Tutorials"

output = testyield()
for i in output:
    print(i)
# Example 2
def generator():
    yield "H"
    yield "E"
    yield "L"
    yield "L"
    yield "O"
test = generator()
for i in test:
    print(i)


# Normal function
def normal_test():
    return "Hello World"
# Generator function
def generator_test():
    yield "Welcome World"
print(normal_test())  # call to normal function
print(next(generator_test()))  # call to generator function
# Print even numbers
# 1. List function
def even_numbers(n):
    for x in range(n):
       if (x%2==0):
           yield x
num = even_numbers(10)
print(list(num))
# 2. for in function
def even_numbers(n):
    for x in range(n):
       if (x%2==0):
           yield x
num = even_numbers(10)
for i in num:
    print(i)
# 3. next function
def even_numbers(n):
    for x in range(n):
       if (x%2==0):
           yield x
num = even_numbers(10)
print(next(num))
print(next(num))
print(next(num))
print(next(num))
print(next(num))
print(next(num))
print('\n')

