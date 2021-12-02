# len method
List = {'Tom': 18, 'Charlie': 12, 'Jany': 25, 'Robert': 25}
print("Length : %d" % len(List))
# variable space
List = {'Tom': 18, 'Charlie': 12, 'Jany': 25, 'Robert': 25}
print("Variable type : %s" % type(List))
# comparison of directory
# List = {'Tom': 18, 'Charlie': 12, 'Jany': 25, 'Robert': 25}
# print()
# str method
List = {'Tom': 18, 'Charlie': 12, 'Jany': 25, 'Robert': 25}
print("Printable string is : %s" % str(List))
# updation of dictionary
List2 = {'Tommy': 4, 'Chinnu': 1, 'Ganga': 5, 'Raj': 2}
List3 = {'Janu': 8, 'Chakki': 2, 'Faj': 7, 'Rinu': 5}
List3.update(List2)
print(List3)
# merge dictionary
Lists = {**List3, **List2}
print(Lists)
# dictionary membership test
print("Tom" in List)
print("Gana" in List2)
# append value to a dictionary
dict1 = {"Name": [], "Address": [], "Age": []}
dict1["Name"].append("Guru")
dict1["Address"].append("Kerala")
dict1["Age"].append("25")
print(dict1)
# accessing dictionary elements
my_dict = {'Name': "Manjusha", 'Age': 25, 'Location': "Kerala"}
print("My name is :", my_dict['Name'])
print("My Location is :", my_dict['Location'])
# deletion of key in dictionary
del my_dict['Location']
print(my_dict)
# pop method
my_dict1 = {'Name': "Manjusha", 'Age': 25, 'Location': "Kerala"}
my_dict1.pop('Age')
print(my_dict1)
# append key to a dictionary like updation
my_dict2 = {'Name': "Anu", 'Age': 25, 'Location': "Goa"}
my_dict2['Name'] = "Aneeshya"
print(my_dict2)
# inserting one dictionary to another
my_dict1['Name'] = my_dict2
print(my_dict1)