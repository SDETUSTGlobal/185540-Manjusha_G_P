mystring = "Meet Guru99 Tutorials Site.Best site for Python Tutorials!"
# find substring
print("The position of site is at:", mystring.find("site"))
print("The position of Tutorials is at:", mystring.find("Tutorials", 20))  # starting position
print("The position of Tutorials is at:", mystring.find("Tutorials", 5, 30))  # starting and ending position
print("The position of Best site is at:", mystring.find("Best site", 5, 40))
print("The position of Guru99 is at:", mystring.find("Guru99", 20))
print("The position of Tutorials using find() : ", mystring.find("Tutorials"))  # find() gives the index of the very first Tutorials substring
print("The position of Tutorials using rfind() : ", mystring.rfind("Tutorials"))  # rfind() gives the last index of substring Tutorials
print("The position of Tutorials using index() : ", mystring.index("Tutorials"))  # index() gives the index of substring Tutorials
# when the substring given is not present in the string
print("The position of Tutorials using find() : ", mystring.find("test"))
#print("The position of Tutorials using index() : ", mystring.index("test"))
# find the total number of times the substring has occurred in the given string
my_string = "test string test, test string testing, test string test string"
startIndex = 0
count = 0
for i in range(len(my_string)):
    k = my_string.find('test', startIndex)
    if k != -1:
        startIndex = k+1
        count += 1
        k = 0
print("The total count of substring test is: ", count )



