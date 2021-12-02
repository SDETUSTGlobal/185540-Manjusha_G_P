# map () using another function
def square(n):
    return n * n
my_list1 = [2, 3, 4, 5, 6, 7, 8, 9]
updated_list = map(square, my_list1)
print(updated_list)
print(list(updated_list))
# map () for variables
my_list2 = [2.6743, 3.63526, 4.2325, 5.9687967, 6.3265, 7.6988, 8.232, 9.6907]
updated_list = map(round, my_list2)
print(updated_list)
print(list(updated_list))
# converting the string given to uppercase
def myMapFunc(s):
    return s.upper()
my_str = "welcome to guru99 tutorials!"
updated_list = map(myMapFunc, my_str)
print(updated_list)
for i in updated_list:
    print(i, end="")
# converting the given tuple to uppercase
def myMapFunc(n):
    return n.upper()
my_tuple = ('php','java','python','c++','c')

updated_list = map(myMapFunc, my_tuple)
print(updated_list)
print(list(updated_list))
# multiply the given number with 10
def myMapFunc(n):
    return n*10
my_list = [2,3,4,5,6,7,8,9]
updated_list = map(myMapFunc, my_list)
print(updated_list)
print(list(updated_list))
# multiply given dictionary values with 10
def myMapFunc(n):
    return n*10
my_dict = {2,3,4,5,6,7,8,9}
finalitems = map(myMapFunc, my_dict)
print(finalitems)
print(list(finalitems))
# lambda function inside the map()
my_list = [2,3,4,5,6,7,8,9]
updated_list = map(lambda x: x * 10, my_list)
print(updated_list)
print(list(updated_list))
#  adding two given lists using map() function
def myMapFunc(list1, list2):
    return list1+list2
my_list1 = [2,3,4,5,6,7,8,9]
my_list2 = [4,8,12,16,20,24,28]
updated_list = map(myMapFunc, my_list1,my_list2)
print(updated_list)
print(list(updated_list))
# Passing one Tuple and a list iterator to map()
def myMapFunc(list1, tuple1):
    return list1+"_"+tuple1

my_list = ['a','b', 'b', 'd', 'e']
my_tuple = ('PHP','Java','Python','C++','C')

updated_list = map(myMapFunc, my_list,my_tuple)
print(updated_list)
print(list(updated_list))