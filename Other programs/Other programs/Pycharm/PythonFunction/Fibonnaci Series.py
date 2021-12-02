# generate the Fibonacci series
def FibonnaciSeries(x):
    c1, c2 = 0, 1
    count = 0
    while count < x:
        yield c1
        c3 = c1 + c2
        c1 = c2
        c2 = c3
        count += 1
fin = FibonnaciSeries(7)
print('Fibonnaci Series')
for i in fin:
    print(i)
# Calling Function with Yield
def test(n):
    return n*n

def getSquare(n):
    for i in range(n):
        yield test(i)

sq = getSquare(10)
for i in sq:
    print(i)
