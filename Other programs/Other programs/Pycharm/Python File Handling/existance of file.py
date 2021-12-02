# Example 1
import os.path
from os import path
print ("File exists:"+str(path.exists('guru99.txt')))
print ("File exists:" + str(path.exists('career.guru99.txt')))
print ("directory exists:" + str(path.exists('myDirectory')))
# Example 2
import pathlib
file = pathlib.Path("guru99.txt")
if file.exists ():
    print ("File exist")
else:
    print ("File not exist")

# check whether a given input is a file or not
print ("Is it File?" + str(path.isfile('guru99.txt')))
print ("Is it File?" + str(path.isfile('myDirectory')))
# check whether a given input is a directory or not
print ("Is it Directory?" + str(path.isdir('guru99.txt')))
print ("Is it Directory?" + str(path.isdir('myDirectory')))


