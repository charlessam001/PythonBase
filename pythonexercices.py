''' name = input("Name: ")
print("Hello, " + name) '''

''' name = input("Name: ")
print(f"Hello, {name}") '''

# a very simple way to write this program above in one line is :
#print(f"Hello, {input("Name: ")}")

'''
num = input("Number: ")
if num > 0:
    print("Number is positive")
elif num < 0:
    print("Number is negative")
else:
    print("Number is 0")
#attiom here because the result should an exception
#so we should do :
num = int(input("Number: "))
'''

''' name = "Harry"
print(name[0])
print(name[1])
'''
'''
# This is a Python comment
names = ["Harry", "Ron", "Hermione"]
# Print the entire list:
print(names)
# Print the second element of the list:
print(names[1])
# Add a new name to the list:
names.append("Draco")
# Sort the list:
names.sort()
# Print the new list:
print(names)

'''
'''
#About tuple
point = (12.5, 10.6)

'''

'''
#About set

# Create an empty set:
s = set()

# Add some elements:
s.add(1)
s.add(2)
s.add(3)
s.add(4)
s.add(3)
s.add(1)

# Remove 2 from the set
s.remove(2)

# Print the set:
print(s)

# Find the size of the set:
print(f"The set has {len(s)} elements.")

""" This is a python multi-line comment of the above code:
Output:
{1, 3, 4}
The set has 3 elements.
"""
'''

'''
#About dictionary

# Define a dictionary
houses = {"Harry": "Gryffindor", "Draco": "Slytherin"}
# Print out Harry's house
print(houses["Harry"])
# Adding values to a dictionary:
houses["Hermione"] = "Gryffindor"
# Print out Hermione's House:
print(houses["Hermione"])
# print houses dictionary
print(houses)

""" Output:
Gryffindor
Gryffindor
"""
'''
'''
#About loops
#for loop
for i in  [0, 1, 2, 3, 4, 5]:
    print(i)

""" Output:
0
1
2
3
4
5
"""
for i in range(6):
    print(i)

""" Output:
0
1
2
3
4
5
"""

# Create a list:
names = ["Harry", "Ron", "Hermione"]

# Print each name:
for name in names:
    print(name)

""" Output:
Harry
Ron
Hermione
"""

name = "Harry"
for char in name:
    print(char)

""" Output:
H
a
r
r
y
"""
'''

'''
#About function:
def square(x):
    return x * x
for i in range(10):
    print(f"The square of {i} is {square(i)}")

""" Output:
The square of 0 is 0
The square of 1 is 1
The square of 2 is 4
The square of 3 is 9
The square of 4 is 16
The square of 5 is 25
The square of 6 is 36
The square of 7 is 49
The square of 8 is 64
The square of 9 is 81
"""
'''






