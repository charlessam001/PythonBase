#About module second file
'''def square(x):
    return x * x
    '''

'''
class Point():
    # A method defining how to create a point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
p = Point(2, 8)
print(p.x)
print(p.y)

""" Output:
2
8
"""
'''
'''
#we create a class that represents an airline flight:
class Flight():
    # Method to create new flight with given capacity
    def __init__(self, capacity):
        self.capacity = capacity
        self.passengers = []

    # Method to add a passenger to the flight:
    def add_passenger(self, name):
        if not self.open_seats():
            return False
        self.passengers.append(name)
        return True

    # Method to return number of open seats
    def open_seats(self):
        return self.capacity - len(self.passengers)
    
    """To comment Note that above, we use the line if not self.open_seats()
    to determine whether or not there are open seats. This works because in Python,
    the number 0 can be interpretted as meaning False, and we can also use the keyword not 
    to signify the opposite of the following statement so not True is False and not False is True.
    Therefore, if open_seats returns 0, the entire expression will evaluate to True
    Now, let’s try out the class we’ve created by instantiating some objects:"""
# Create a new flight with o=up to 3 passengers
flight = Flight(3)

# Create a list of people
people = ["Harry", "Ron", "Hermione", "Ginny"]

# Attempt to add each person in the list to a flight
for person in people:
    if flight.add_passenger(person):
        print(f"Added {person} to flight successfully")
    else:
        print(f"No available seats for {person}")

""" Output:
Added Harry to flight successfully
Added Ron to flight successfully
Added Hermione to flight successfully
No available seats for Ginny
"""
'''
'''
#About decorator:
"""decorator is a higher-order function that can modify another function :"""
def announce(f):
    def wrapper():
        print("About to run the function")
        f()
        print("Done with the function")
    return wrapper

@announce
def hello():
    print("Hello, world!")

hello()

""" Output:
About to run the function
Hello, world!
Done with the function
"""
'''
'''

#About lamda
#Lambda functions provide another way to create functions in python.
#square = lambda x: x * x

"""
people = [
    {"name": "Harry", "house": "Gryffindor"},
    {"name": "Cho", "house": "Ravenclaw"},
    {"name": "Draco", "house": "Slytherin"}
]

def f(person):
    return person["name"]

people.sort(key=f)

print(people)

""" Output:
[{'name': 'Cho', 'house': 'Ravenclaw'}, {'name': 'Draco',
 'house': 'Slytherin'}, {'name': 'Harry', 'house': 'Gryffindor'}]
 """
 """
#The same code by using lamda function:
people = [
    {"name": "Harry", "house": "Gryffindor"},
    {"name": "Cho", "house": "Ravenclaw"},
    {"name": "Draco", "house": "Slytherin"}
]

people.sort(key=lambda person: person["name"])

print(people)

""" Output:
[{'name': 'Cho', 'house': 'Ravenclaw'}, {'name': 'Draco', 'house': 'Slytherin'},
 {'name': 'Harry', 'house': 'Gryffindor'}]
"""
'''
#About exception:
"""
x = int(input("x: "))
y = int(input("y: "))

result = x / y

print(f"{x} / {y} = {result}")
"""
#In many cases, this program works well
#However, we’ll run into problems when we attempt to divide by 0
#We can deal with this messy error using Exception Handling. In the following block of code,
#we will try to divide the two numbers, except when we get a ZeroDivisionError:
import sys

x = int(input("x: "))
y = int(input("y: "))

try:
    result = x / y
except ZeroDivisionError:
    print("Error: Cannot divide by 0.")
    # Exit the program
    sys.exit(1)

print(f"{x} / {y} = {result}")
#However, we still run into an error when the user enters non-numbers for x and y:
#We can solve this problem in a similar manner!
import sys

try:
    x = int(input("x: "))
    y = int(input("y: "))
except ValueError:
    print("Error: Invalid input")
    sys.exit(1)

try:
    result = x / y
except ZeroDivisionError:
    print("Error: Cannot divide by 0.")
    # Exit the program
    sys.exit(1)

print(f"{x} / {y} = {result}")
