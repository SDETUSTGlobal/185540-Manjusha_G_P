a = 2021
b = "Welcome"
print(b + " " + str(a))
f = 101
e = 201


def somefunction():
    global f
    print(f)
    f = "Python"
    print(f)


somefunction()
print(e)
