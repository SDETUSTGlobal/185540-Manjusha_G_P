# strip() Method in Python
str = "Welcome to Python!"
after_strip = str.strip()
print(after_strip)
# strip() on Invalid Data Type
#mylist = ["a", "b", "c", "d"]
#print(mylist.strip())
# strip() Passing character parameters
str1 = "****Welcome to Python!****"
after_strip = str1.strip("*")
print(after_strip)
str2 = "Welcome to Python!"
after_strip1 = str2.strip("to")
print(after_strip1)
str3 = "Welcome to Python!"
after_strip3 = str3.strip("Welcome")
print(after_strip3)