number = {'one': 1, 'two': 2}
check = {'one': 1, 'two': 2}
boys = {'Tommy': 18, 'Jin': 17, 'Jeevan': 18}
girls = {'Sara': 14, 'Sheena': 14, 'Sana': 15}
# copy
stuB = boys.copy()
styG = girls.copy()
print(styG)
print(stuB)
# update
number.update({'three': 3})
print(number)
# delete
del number['one']
print(number)
# items method
print("Student Name: %s" % boys.items())
for key in check.keys():
    if key in number.keys():
        print("True")
    else:
        print("False")
