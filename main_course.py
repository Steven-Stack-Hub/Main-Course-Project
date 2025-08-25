import random

def get_choices():
    #player_choice = input("Enter a choice (rock, paper, scissors): ")

    options = ["rock", "paper", "scissors"]
    computer_choice = random.choice(options)
    choices = {"player": "rock", "computer": computer_choice}
    return choices 

def check_win(player, computer):
    print(f"You chose {player}, computer chose {computer}")
    if player == computer:
        return "It's a tie!"
    elif player == "rock":
        if computer == "scissors":
            return "Rock smashes scissors! You win!"
        else:
            return "Paper covers rock! You lose."
    elif player == "paper":
        if computer == "rock":
            return "Paper covers rock! You win!"
        else:
            return "scissors cuts paper! You lose."
    elif player == "scissors":
        if computer == "paper":
            return "scissors cuts paper! You win!"
        else:
            return "Rock Smashes Scissors! You lose."

choices = get_choices()
result = check_win(choices["player"], choices["computer"])
name = "Steven"
print(name.upper())  # this is an inline comment
print(type(name))  # this is a function to print the type of the variable

print(
    isinstance(name, str)
)  # this is a function to print the type of the variable to see if it is a string

age = float(3.9)  # this is a float

print(age)  # this is a float

print(isinstance(age, float))

age = 3, 2.5,  # This is a Tuple

print(age)

print(type(age))

print(
    isinstance(age, tuple)
)  # this is a function to print the type of the variable to see if it is a tuple

age = (20)  # this is an integer

print(
    isinstance(age, int)
)  # this is a function to print the type of the variable to see if it is an integer

#Arithmetic Operators
print(1 + 1)  # Addition
print(2 - 1)  # Subtraction
print(2 * 2)  # Multiplication
print(9 / 3)  # Division
print(5 % 2)  # Modulus
print(2**3)  # Exponentiation
print(5 // 2)  # Floor Division

age = 8
age += 8
print(age)  # age = age + 8

#Comparison Operators
a = 5
b = 10

print(a == b)  # Equal to
print(a != b)  # Not equal to
print(a > b)  # Greater than
print(a < b)  # Less than
print(a >= b)  # Greater than or equal to
print(a <= b)  # Less than or equal to


#Ternary Operator, The Slower Way
age = 22  # Corrected: added an assignment to age before it is used

if age > 18:
    print("Adult")
else:
    print("Not Adult")


#Ternary Operator, The Faster Way
def is_adult(age):
    return True if age > 18 else False  # This is a faster way to do it, which is called a ternary operator


#Strings
"Beau"  # This is a string
'Beau'  # This is a string
name = "Beau" 
name += " is my name"  # This is a string concatenation meaning adding this string to another string
age = str(20)
print(name)
print("""Beau is 
20 years old""")

print("Beau".upper())
print("Beau".lower())
print("BEAU pERSon".title())
print("BEAU".islower())


def isalpha():
    #This is a function to check if the string contains only characters and is not empty
    pass


def isalnum():
    #This is a function to check if the string contains only characters and numbers (and is not empty)
    pass


def isdecimal():
    #This is a function to check if the string contains only decimal characters and is not empty
    pass


def lower():
    #This is a function to convert a string to lowercase
    pass


def islower():
    #This is a function to check if the string is in lowercase
    pass


def upper():
    #This is a function to convert a string to uppercase
    pass


def isupper():
    #This is a function to check if the string is in uppercase
    pass


def title():
    #This is a function to convert a string to title case
    pass


def startswith():
    #This is a function to check if the string starts with a specified value
    pass


def endswith():
    #This is a function to check if the string ends with a specified value
    pass


def replace():
    #This is a function to replace a specified value with another value in a string
    pass


def split():
    #This is a function to split a string into a list where each word is a list item
    pass


def strip():
    #This is a function to remove any whitespace from the beginning or the end of a string
    pass


def join():
    #This is a function to join a list into a string, with a specified separator between each item
    pass


def find():
    #This is a function to search for a specified value in a string and returns the position of where it was found
    pass


name = "Beau is my name"
print(name.lower())  # This is a function to convert a string to lowercase
print(len(name))
print(
    "au" in name
)  # This is a function to check if a string is in another string(Also called a substring)

#Escaping Characters
name = "Be\"lax"  # In this line we have a double quote inside a string
print(name)

name = 'Be"\"lax'  # In this line we have both a double quote in the middle of the string and a single quote outside the string
print(name)

name = 'Be\nau'  # \N = a newline character

print(name)

name = "Be\\au"  # In This line we have the second backslash, which is used to escape the first backslash so it prints out the name with the hasmark and not without the a like Beu.
print(name)

name = "Be\"aux\"au"  #This is a Hashmark comment for the term escaping, in this line we have a double quote inside a string

print(name.upper())  # this is an inline comment

# String Characaters And Slicing
name = 'Beau is cool'
print(name[-4:9])  # This is a function to print characters from the string
#Strings are false only if they are empty

#Booleans

done = True  # This is a boolean variable. it defines any value as the chance to be true if it is either a number or a character otherwise if it says nothing like 0 or an empty string it will be false

print(type(done) == bool)  # This is a function to print the type of the variable to see if it is a boolean basically a true or false statement
if done:
    print("Yes, it is done") # Basically a option result based on the condition of the variable
else:
    print("No, it is not done")  # This is a function to print the condition if it is true or false basically a option result based on the condition of the variable

book_1_read = True
book_2_read = False

read_any_book = any([
    book_1_read, book_2_read
])  # This is a function to check if any of the variables are true

ingredients_purchased = True
meals_cooked = False

ready_to_serve = all([ingredients_purchased, meals_cooked])

#Number Data Types

num1 = 2 + 3j  # This is a complex number
num2 = complex(2, 3)  # This is a complex number
print(
    num2.real, num2.imag
)  # This is a function to print the real and imaginary parts of a complex number

# Built in Functions
print(round(5.445,
            2))  # This is a function to round a number to the nearest integer

#Enums - These are readable names bound to a constant value. Enums are great for things that you know aren't going to change, like months, days, colors, etc.

from enum import Enum


class Stat(Enum):  # This is a class to create an enum
    ACTIVE = 3


print(Stat.ACTIVE.value)  # This is a function to print the value of the enum
print(list(Stat))  # This is a function to print the list of the enum basically the name of the enum
print(len(Stat))

# User Input: This is a function to get input from the user
age = input("What is your age? ")
print("Your age is " + age)

#Control Statement: # This is a function to check if a condition is true or false
condition = False

if condition is True:
    print("The condition")
    print("was True")  # This is a function to print the condition if it is true basically a option result based on the condition of the variable

condition = False
name = 'Flavio'

if condition == True:
    print("The condition")
    print("was True")
elif name == 'Roger':
    print("Hello Roger")
elif name == 'Syd':
    print("Hello Syd")
elif name == "Flavio":
    print("Hello Flavio") 

#Lists: A list is a collection which is ordered and changeable. Allows duplicate members.
dogs = ["Roger", 1, "Syd", True]  # This is a list

print (dogs[2])

print( "Syd" in dogs) # This is a function to check if an item is in a list(Like a Boolean Result)

print(dogs[0:4])

dogs[1] = "Dave"
print(dogs)
print(dogs[2:4]) # This is a function to print a range of items in a list
print(dogs[0:3]) 
print(dogs[0:])
dogs.append("Judah") # This is a function to add an item to the end of the list
print(dogs)
print(len(dogs)) # This is a function to print the length of strings in the list
dogs.extend(['Jimmy', 'Vito']) # You can also use the += operator to add two lists together instead of extend
print(dogs)
dogs.remove('Roger') # This is a function to remove an item from the list
print(dogs)

print(dogs.pop()) # This is a function to remove the last item from the list and return it
print
print(dogs)

items = ['Roger', 'Syd', 'Flavio', 'Flavio', 'Roger'] 
print(items)
items.insert(1, 'Test') # This is a function to insert an item into the list at a specific index, which is in this case 1
print(items)

items[1:1] = ['Test1', 'Test2'] # This is a way to insert multiple items into a list
print(items) 

#Sorting Lists: This is a function to sort a list in alphabetical order
items = ['Roger', 'Zion', 'Flavio', 'flavio', 'Roger']
items.sort() # This is a function to sort a list in its order and automatically makes the first letter uppercase and the rest lowercase. It puts 'flavio' at the end because everything else is uppercase and it is lowercase, and is also aware of the alphabetical order.
itemscopy = items[:] # This is a function to copy a list
print(items)
items.sort(key=str.lower) # This is a function to sort a list in alphabetical order ignoring uppercase letters and lowercase letters and numbers 
print(items)
print(itemscopy) # This is a copy of the origiinal Sorted List with undercase 'flavio' at the end

# Tuples: A tuple is a collection which is ordered and unchangeable. Allows duplicate members.
names = ("Roger", "Syd", "Flavio")  #
print(names)
names[-1]
names.index("Roger") # This is a function to find the index of an item in a tuple, basically the position of the item in the tuple

len(names)

print("Roger" in names)
print(sorted(names)) # This is a function to sort a tuple in alphabetical order
newTuple = names + ("Tina", "Rufus") # This is a function to add a tuple to another tuple

print(newTuple)

# Dictionaries: A dictionary is a collection which is unordered, changeable and indexed. No duplicate members.
dog = {"name":"Roger", "age": 8, "color": "Green"}  # This is a dictionary

print(dog.get("name")) # This is a function to obtain the value of a key in a dictionary

print(dog.get("color", "brown")) # This is a function to obtain the default value of a key if it is not in the dictionary. In this case the default value is brown, if it cannot find the targeted value in the dictionary it will print the defaulted value, Brown.

print(dog.pop("name")) # This is a function to remove a key from a dictionary and return its value outside of the dictionary
print(dog)

print(dog.popitem()) # This is a function to remove the last key from a dictionary and return its value outside of the dictionary basically the last item in the dictionary

print(dog)

print ("color" in dog) # This is a function to check if a key is in a dictionary, like a boolean value, in this case it is false because wee removed the last iitem from the dictionary and printed it outside of the dictionary

print(dog.keys()) # This is a function to print the keys of a dictionary, so far we only have age, because we popped the name and popitemed color out of the dictionary

print(list(dog.keys())) # The diffeerence between this and the previous line is that this line is a list of the keys of the dictionary and the previous line is a dictionary of the keys of the dictionary

print(list(dog.items())) # This is a function to print the items of a dictionary, which is a list of tuples
print(len(dog))

dog["favorite food"] = "Meat" # This is a function to add a key to a dictionary and give it a value
print(dog)

del dog['age'] # This is a function to delete a key from a dictionary
print(dog)

dogCopy = dog.copy() # This is a function to copy a dictionary
print(dog) 
age = 30
if age > 18:
    print("You are an adult")

    
#Sets: A set is a collection which is unordered and unindexed. In Python sets are written with curly brackets.


set1 = {"Roger", "Syd", "Roger"} # This is a set, which is a collection of unique items, which is why Roger is only printed once. There can only be one of each item value in a set.

set2 = {"Sally"}


print(list(set1))
mod = set1 | set2 # This is a function to print the union of two sets, which is all the items in both sets, in this case it is Roger, Syd, Sally
mod = set1 > set2
mod = set1 < set2
print(len(set2))
print(set2)
print(mod) # This is a function to print the intersection of two sets, which is the common items in both sets, in this case it is Roger and Syd. And "mod" is the variable name for the intersection of the two sets

#Functions: A function is a block of code which only runs when it is called. You can pass data, known as parameters, into a function. A function can return data as a result.

def hello(name, age = "my friend"):
    print("Hello " + name + ", you are " + str(age) + " years old") # This is a function to print a string with a variable in it, in this case the variable is name and age. so basically it will print "Hello Beau, you are 28 years old" for the first function call.

hello("Beau", 28)
hello("Quincy", 31)
hello("Flavio", 39)
hello("Sean", 40)

#Conditional Statement to assign default value for age if it's not given
def hello(name, age = "my friend"): #
    if age == "my friend": # This is a conditional statement to check if the age is the default value, if it is then it will print the first line, if it is not then it will print the second line. So basically it will print "Hello Adam, you are my friend" for the first function call, Since it is the default value, When the "age" is not given a value it will print the default value, which is "my friend". And if the age is given a value it will print the second line, which is "Hello Adam, you are 28 years old" for the second function call.
        print("Hello " + name + ", you are " + age)
    else:
        print("Hello " + name + ", you are " + str(age) + " years old") #Fix: Added str() to convert age to a string
hello("Adam")

def change(value):
    value["name"] = "Syd"

val = {"name": "Tom"} # The dictionary is called first before the value["name"] = "Syd" function is called, so the change function is called after the dictionary is created.
change(val)

print(val)
# "hello()" # This will result in a TypeError 'missing 1 required positional argument, only if it doesn't call the function name like the other 2 functions, or there is no default(else) option argument to print out if it isn't called, because you are trying to call a function with no arguments when it does requires one argument in this case "name" and there would be no default value for it.


#Functions(Return Statments)
#Return Statements are used to return a value from a function.
def hello(name):
    if not name:
        return
    print("Hello " + name + "!")
    return name, "Larson", 8

print(hello("Solly"))

#Variable Scope

age = 8 

def test():
    age = 8 #This is a local variable, which is only available inside the function. Without the `global age` declaration, this `age` is a *different* variable than the `age` defined outside the function.  It *shadows* the outer `age`. Basically it is a variable that is only available inside the function, and it is not available outside the function, which is why it is called a local variable, and will result in a NameError if you try to access it outside the function.
    
    print(age)
print(age) #8
test()#8


#Nested Functions 
# Nested Functions are functions that are defined inside other functions. They are only available inside the function that they are defined in.


def talk(phrase): # This is a function to print a phrase
    def say(word): # This is a nested function to print a word
        print(word) # This is a function to print a word
    words = phrase.split(' ') # This is a function to split a string into a list of words
    for word in words: # This is a for loop to iterate through the list of words
        say(word) # This is a function to print a word

talk('I am going to buy the milk') # This is a function call to print a phrase

def count(): # This is a function to count
    count = 0 # This is a variable to store the count
    def increment(): # This is a nested function to increment the count
        nonlocal count # This is a function to access the variable count from the outer scope
        count = count + 1 # This is a function to increment the count
        print(count) # This is a function to print the count
    increment() # This is a function call to increment the count

count() # This is a function call to count

#Closures

def increment(): # This is a function to increment
    def counter(): # This is a nested function to count
        count = 0 # This is a variable to store the count
        def increment(): # This is a nested function to increment the count
            nonlocal count  # This is a function to access the variable count from the outer scope
            count = count + 1 # This is a function to increment the count
            return count # This is a function to return the count

        return increment # This is a function to return the increment

print(increment()) #1 # This is a function call to increment and print the count
print(increment()) #2 # This is a function call to increment and print the count
print(increment()) #3 # This is a function call to increment and print the count

#Objects
 #Objects are instances of classes. They are created by calling the class.

age = 8 # This is an object of the int class
print(age.real) # This is a function to print the real part of the object

print(age.imag) # This is a function to print the imaginary part of the object

print(age.bit_length()) # This is a function to print the bit length of the object, which is the number of bits required to represent the object in binary. And bits are the smallest unit of data in a computer, which is either a 0 or a 1. So the bit length of 8 is 4, because 8 is 1000 in binary, and there are 4 bits in 1000.

items = [1, 2] # This is an object of the list class

items.append(3) # This is a function to add an item to the list

items.pop() # This is a function to remove the last item from the list and return it outside of the list

print(id(items)) # This is a function to print the id of the object, which is the memory address of the object.

age = age + 1

#Loops: Loops are used to iterate over a sequence (that is either a list, a tuple, a dictionary, a set, or a string).

condition = True
while condition == True:
    print("The condition is True")
    condition = False # This is a function to change the condition to False, so the loop will stop running.

count = 0
while count < 10:
    print("The condition is True")
    count = count + 1 # This is a function to increment the count by 1, so the loop will stop running after 10 iterations.

print("After the loop")

items = [1, 2, 3, 4]
for item in items:
    print(item) # This is a function to print each item in the list, basically a for loop to iterate through the list and print each item.

for item in range(15):
    print(item) # This is a function to print the numbers from 0 to 14, because the range function is inclusive of the start and exclusive of the end. So it will print the numbers from 0 to 14, but not 1

items = ["Beau", "Roger", "Syd"]
for index, item in enumerate(items): # This is a function to iterate through a list and print the index and the item, basically the position of the item in the list and the item itself.
    print(index, item) # This is a function to print the index and the item, basically the position of the item in the list and the item itself.

items = [1, 2, 3, 4]
for item in items: # This is a for loop to iterate through the list of items
    if item == 2:
        continue # This is a function to skip the current iteration of the loop and continue with the next iteration.
    print(item)
    
items = [1, 2, 3, 4]
for item in items:
    if item == 2:
        break # This is a function to break out of the loop and stop the loop from running.
    print(item)

#Classes: Classes are used to create objects. They are blueprints for objects. They are used to create objects with the same properties and methods.

class Animal:
    def walk(self):
        print("Walking...") # This is a method to print a string, basically a function that is defined inside a class.


class Dog(Animal):
    def __init__(self, name, age): # This is a constructor, which is a special method that is called when an object is created. It is used to initialize the object.
        self.name = name # This is a property of the object, which is a variable that is associated with the object.
        self.age = age # This is a property of the object, which is a variable that is associated with the object.
        
    def bark(self): # This is a method to print a string, basically a function that is defined inside a class.
        print("Woof!")

roger = Dog("Roger", 8) # This is an object of the Dog class, which is an instance of the Dog class. It is created by calling the Dog class and passing in the name and age of the dog.

print(roger.name) # This is a function to print the name of the object, which is the name of the dog.

roger.bark()

roger.walk() # This is a function to call the walk method of the object, which is the walk method of the Dog class.

print(type(roger)) # This is a function to print the type of the object, which is the class that the object is an instance of.


#Base Classes: Base classes are classes that are inherited by other classes. They are used to create objects with the same properties and methods. They are used to create objects with the same properties and methods.

#Inheritance: Inheritance is a way to create a new class using classes that have already been defined. The newly formed classes are called derived classes, the classes that we derive from are called base classes. Important benefits of inheritance are code reuse

#Modules: Modules are files that contain Python code. They are used to organize code into reusable pieces. They are used to import code from other files. They are used to import code from other modules. They are used to import code from other packages.


#From lib.dog import bark
#bark()

#from lib import dog
#dog.bark()

from math import sqrt
print(sqrt(4))


#Imports: Imports are used to import code from other files. They are used to import code from other modules. They are used to import code from other packages.

#Packages: Packages are folders that contain modules. They are used to organize code into reusable pieces. They are used to import code from other files. They are used to import code from other modules. They are used to import code from other packages.


#Accepting Arguments: Accepting arguments is a way to pass data into a function, which is a block of code that is executed when it is called. 
#import sys
#print(sys.argv)    
#print("Hello" + name)

import argparse

parser = argparse.ArgumentParser(description="This program prints the name of my dogs")


parser.add_argument('-c', '--color', metavar='color', required=False, choices=['red', 'yellow'], help='the color to search for')

args = parser.parse_args()

if args.color:
    print(f"The desired color is: {args.color}")
else:
    print("No color specified.")

#Lambda Functions: Lambda functions are anonymous functions, which means they are functions that are not bound to a name. They are used to create small anonymous functions. 

lambda num : num * 2 # This is a lambda function to multiply a number by 2, so basically a lambda function makes a function that takes a number and returns the number multiplied by 2.

def multiply(a, b):
    return a * b

print(multiply(2, 4))

#Map(), Filter(), Reduce() : Map, filter, and reduce are functions that are used to apply a function to a sequence of elements.


#Map(): Map is a function that applies a function to a sequence of elements. It returns a new list with the results of applying the function to each element in the sequence.
numbers = [1, 2, 3, 4, 5]

def double(a): # This is a function to double a number, which is a lambda function that takes a number and returns the number multiplied by 2.
    return a * 2
result = map(double, numbers)
print(list(result))

numbers = [1, 2, 3,]

result = map(lambda a : a * 2, numbers)
print(list(result))

#Filter(): Filter is a function that applies a function to a sequence of elements. It returns a new list with the results of applying the function to each element in the sequence.

numbers = [1, 2, 3,]

def isEven(n):
    return n % 2 == 0

result = filter(isEven, numbers)
    
print(list(result))

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

result = filter(lambda n : n % 2 == 0, numbers)

print(list(result))


#Reduce(): Reduce is a function that applies a function to a sequence of elements. It returns a single value, which is the result of applying the function to each element in the sequence.

from functools import reduce

expenses = [ 
('Dinner', 80), 
('Car Repair', 120)
]

sum = reduce(lambda a, b : a[1] + b[1], expenses) # This is a lambda function to add the second element of each tuple in the list, which is the cost of the expense. Basically it is a lambda function that takes two tuples and returns the sum of the second element of each tuple.

print(sum)


# Recursion

# 3! = 3 * 2 * 1 = 6
# 4! = 4 * 3 * 2 * 1 = 24
# 5! = 5 * 4 * 3 * 2 * 1 = 120

def factorial(n): # This is a function to calculate the factorial of a number, which is the product of all positive integers less than or equal to that number.
    if n == 1:
        return 1
    return n * factorial(n - 1)
print(factorial(5))

#Decorators: Decorators are a way to modify the behavior of a function. They are used to add functionality to a function.
def logtime(func): # This is a decorator to log the time it takes to run a function.
    def hello():
        print("Hello!")

def logtime(func):
    def wrapper():
        print("Before")
        val = func()
        print("After")
        return val
    return wrapper
    
@logtime
def hello():
    print("Hello!")

hello()


#Docstrings: Multi-line strings used for documenting code (functions, classes, modules).  They are accessed using `help(object)` or `object.__doc__`. Follow a consistent format for readability.

def increment(n):
    """Increment a number"""
    return n + 1

class Dog:
    """A class representing a dog"""
    def __init__(self, name, age):
        """Initialize a new dog"""
        self.name = name
        self.age = age
    def bark(self):
        """Let the dog bark"""
        print("Woof!")
        print(help(Dog))
    def __init__(self, name, age):
        """Initialize a new dog"""
        self.name = name
        self.age = age
        def bark(self):
            """Let the dog bark"""
            print("Woof!")
            print(help(Dog))


#Annotations: Function annotations are arbitrary python expressions that are associated with various part of functions. They are used to type check the functions by third party tools. They are used to specify the type of the arguments and the return value of the function. They are basically a way to add metadata to the function.

def increment(n: int) -> int:
    return n + 1
    
count: int = 0


#Exceptions: Exceptions are errors that occur during the execution of a program. They are used to handle errors that occur during the execution of a program. They are used to handle errors that occur during the execution of a program. They are used to

try: # This is a try block to catch exceptions, which is a block of code that is executed if an exception occurs.
    result = 2 / 0
except ZeroDivisionError:
    print("Cannot divide by zero")
    result = 0 # Assign a value to result in case of an exception
finally:
    print("This will always execute")

#result = 2 / 0 #Causes ZeroDivisionError, now inside try-except block
#print(result) # Will cause an error if the above line is uncommented
try: # This is a try block to catch exceptions, which is a block of code that is executed if an exception occurs.
    result = 2 / 0
except ZeroDivisionError:
    print("Cannot divide by zero")
    result = 0 # Assign a value to result in case of an exception
finally:
    pass  # No need to reassign result here

print(result)

try:
    raise Exception("An error occurred") # This is a raise statement to raise an exception, which is a statement that is used to raise an exception. It is used to raise an exception that is not handled by the program.
except Exception as error:
    print(error)
class DogNotFoundException(Exception):
    print('Inside')
    pass
try:
    raise DogNotFoundException
except DogNotFoundException:
    print("Dog not found")

filename = '/Users/flavio/test.txt'

try:
    file = open(filename, 'r')
    content = file.read()
    print(content)
except FileNotFoundError:
    print(f"Error: The file '{filename}' was not found.")
except Exception as e:
    print(f"An error occurred: {e}")
finally:
    if 'file' in locals() and hasattr(file, 'close'):
        file.close()
        
    print("Closing file")

filename = '/Users/flavio/test.txt'

try:
    with open(filename, 'r') as file:
        content = file.read()
        print(content)
except FileNotFoundError:
    print(f"Error: The file '{filename}' was not found.")
except Exception as e:
    print(f"An error occurred: {e}")

# Pip is a package manager for Python. It is used to install and manage packages. 

# Terminal Commands for pip:

# pip install requests

# pip install -U requests

# pip uninstall requests

# pip show requests 


# List Compressions: List comprehensions are a way to create lists. They are used to create lists from other lists. 

numbers = [1, 2, 3, 4, 5]

numbers_power_2 = [n**2 for n in numbers] # This is a list comprehension to create a list of the squares of the numbers in the list.

print(numbers_power_2)

numbers_power_2 = []
for n in numbers: # This is a for loop to iterate through the list of numbers and append the square of each number to the list of squares.
    numbers_power_2.append(n**2) # This is a function to append the square of each number to the list of squares.

numbers_power_2 = list(map(lambda n: n**2, numbers)) # This is a map function to create a list of the squares of the numbers in the list.

# Polymorphism: Polymorphism is the ability of different classes to be treated as instances of the same class through inheritance.

class Animal:
    def speak(self):
        print("Generic animal sound")

    def eat(self):
        print("Generic animal eating")

class Dog(Animal):
    def speak(self):
        print("Woof!")

    def eat(self):
        print("Eating dog food")


class Cat(Animal):
    def speak(self):
        print("Meow!")

    def eat(self):
        print("Eating cat food")

animal1 = Dog()
animal2 = Cat()

animal1.eat()
animal2.eat()


#Operator Overloading: Operator overloading is a way to change the behavior of an operator.

class Dog:
    # the dog class
    def __init__(self, name, age): # This is a constructor, which is a special method that is called when an object is created. It is used to initialize the object. Basically it is a function that is called when an object is created.
        self.name = name # This is a property of the object, which is a variable that is associated with the object.
        self.age = age

    def __gt__(self, other):
        return self.age > other.age  # This is a greater than operator to compare the age of two dogs.


roger = Dog("Roger", 8)
syd = Dog("Syd", 7)
#__add__() responds to the + operator
#__sub__() responds to the - operator
#__mul__() responds to the * operator
#__truediv__() responds to the / operator
#__floordiv__() responds to the // operator
#__mod__() responds to the % operator
#__pow__() responds to the ** operator
#rshift() responds to the >> operator
#lshift() responds to the << operator
#__and__() responds to the & operator
#__or__() responds to the | operator
#__xor__() responds to the ^ operator
#Telusko : Dictionaries in Python
data = {'Navin':'Python', 'Kiran':'Java', 'Harsh':'JS'}
print(data['Navin'])
print(data['Harsh'])
print(data.get('Navin'))
print(data.get('Harsh'))
print(data.get('Harsh'))
print(data.get('Monika', 'Not Found'))
print(data.get('Harsh', 'Not Found'))
keys = ['Navin', 'Kiran', 'Harsh']
values = ['Python', 'Java', 'JS']
data = dict(zip(keys, values))
print(data)
#data ['Kiran'] #This will result in a TypeError because you are trying to access a dictionary with a value instead of a key

#data['Monika'] = 'CS' #This will result in a KeyError because you are trying to access a dictionary with a key that does not exist

#del data['Harsh'] #This will result in a KeyError because you are trying to delete a key that does not exist

data = {'Navin':'Python', 'Kiran':'Java', 'Harsh':'JS'}
print(data['Navin'])
data = {'Navin':'Python', 'Kiran':'Java', 'Harsh':'JS'}
print(data.get('Navin'))
prog = {'JS':'Atom', 'CS':'VS', 'Python':['Pycharm', 'Sublime'], 'Java':{'JSE':'Netbeans', 'JEE':'Eclipse'}}
print(prog['JS'])
prog = {'JS':'Atom', 'CS':'VS', 'Python':['Pycharm', 'Sublime'], 'Java':{'JSE':'Netbeans', 'JEE':'Eclipse'}}

#Telusko: More Variables in Python 

num = 5 # Assigns the integer value 5 to the variable num

print(id(num)) # Prints the memory address of the variable num

name = 'Steven' # Assigns the string value 'Steven' to the variable name

print(id(name)) # Prints the memory address of the variable name

a = 10 

b = a # Assigns the value of a (which is 10) to the variable b

print(id(a)) 

print(id(b))

print(id(10)) # Prints the memory address of the integer literal 10

k = 10 # Assigns the integer value 10 to the variable k

print(id(k)) # Prints the memory address of the variable k

a = 9 

print(id(a)) # Prints the memory address of the variable a

print(id(b)) # Prints the memory address of the variable b (still points to the original 10)

k = a # Assigns the value of a (which is now 9) to the variable k

print(id(k)) # Prints the memory address of the variable k

b = 8 # Assigns the integer value 8 to the variable b

PI = 3.14 # Assigns the float value 3.14 to the variable PI

PI = 3.15 # Assigns the float value 3.15 to the variable PI, overwriting the previous value

print(type(PI)) # Prints the data type of the variable PI

#Telusko: Data Types in Python

num = 2.5 # Assigns the float value 2.5 to the variable num

print(type(num)) # Prints the data type of the variable num, which is float

num = 5 # Assigns the integer value 5 to the variable num, overwriting the previous value

print(type(num)) # Prints the data type of the variable num

num = 6 + 9j  #This is a complex number, assigning the complex number 6 + 9j to the variable num

a = 5.6 # Assigns the float value 5.6 to the variable a

b = int(a) # Converts the float value of a to an integer and assigns it to the variable b

print(type(b)) # Prints the data type of the variable b, which is int

k = float(b) # Converts the integer value of b to a float and assigns it to the variable k, which is 5.0

print(k) # Prints the value of the variable k

k = 6 # Assigns the integer value 6 to the variable k

c = complex(b, k) # Creates a complex number using b and k as real and imaginary parts, respectively, and assigns it to c

bool = b < k # Checks if b is less than k and assigns the boolean result to the variable bool

print(type(bool)) # Prints the data type of the variable bool

bool = b > k # Checks if b is greater than k and assigns the boolean result to the variable bool, which is False

print(int(True)) # Prints the integer representation of True (which is 1)

print(int(False)) # Prints the integer representation of False (which is 0)

lst = [25, 36, 45, 55] # Creates a list of integers and assigns it to the variable lst

a = (25, 36, 45, 55) # Creates a tuple of integers and assigns it to the variable a

print(type(a)) # Prints the data type of the variable a

t = (25, 36, 45, 55) # Creates a tuple of integers and assigns it to the variable t

print(type(t)) # Prints the data type of the variable t

str = "Steven" # Assigns the string value "Steven" to the variable str

st = 'a' # Assigns the string value 'a' to the variable st

print(type(st)) # Prints the data type of the variable st, which is str

print(range(0, 10)) # Prints a range object from 0 to 9

print(list(range(10))) # Converts the range object to a list and prints it

print(list(range(2, 10, 2))) # Creates a list of even numbers from 2 to 8 and prints it

print(type(range(10))) # Prints the data type of range(10), which is the range class

d = {'Steven':'Samsung', 'Kim' : 'iphone', 'John' : 'Pixel' } # Creates a dictionary with string keys and values

print(d.keys()) # Prints the keys of the dictionary d, which is ['Steven', 'Kim', 'John']

print(d.values()) # Prints the values of the dictionary d, which is ['Samsung', 'iphone', 'Pixel']

print(d['Kim']) # Prints the value associated with the key 'Kim' in the dictionary d, which is 'iphone'

print(d.get('John')) # Prints the value associated with the key 'John' in the dictionary d, which is 'Pixel'

#Telusko: Operators in Python
# Covering: Arithmetic (Increment, Multiplication, Division, Subtraction), Comparison(Greater Than, Less Than, Equal To Operators), Logical, Bitwise, Assignment, Negation(Unary), Operator


x = 2 # Assigns the integer value 2 to the variable x

y = 3 # Assigns the integer value 3 to the variable y

print(x-y) # Prints the result of subtracting y from x, which is -1

print(x*y) # Prints the result of multiplying x and y, which is 6

print(x/y) # Prints the result of dividing x by y, which is 0.6666666666666666

x = x + 2 # Adds 2 to the current value of x and assigns the result back to x

x += 2 #This is an increment operator, basically it is the same as x = x + 2, Adds 2 to the current value of x and assigns the result back to x

print(x) # Prints the value of x

x *= 3 #This is a multiplication operator, basically it is the same as x = x * 3, Multiplies the current value of x by 3 and assigns the result back to x

print(x) # Prints the value of x

a,b = 5,6 # Assigns the value 5 to a and 6 to b in a single line

n = 7 # Assigns the integer value 7 to the variable n

print(n) # Prints the value of n

print(-n) # Prints the negation of n

n = -n #This is a negation operator, basically it is the same as n = -n, Negates the value of n and assigns it back to n

print(n) # Prints the value of n

print(a < b) # Checks if a is less than b and prints the boolean result

print(a > b) # Checks if a is greater than b and prints the boolean result

print(a == b) # Checks if a is equal to b and prints the boolean result

a = 6 # Assigns the integer value 6 to the variable a

print(a == b) #This is a comparison operator, basically it is a equal to operator, basically it is the same as a == b, Checks if a is equal to b and prints the boolean result

print(a <= b) #This is a comparison operator, basically it is a less than or equal to operator, basically it is the same as a <= b, Checks if a is less than or equal to b and prints the boolean result

print(a != b) #This is a comparison operator, basically it is a not equal to operator, basically it is the same as a != b, Checks if a is not equal to b and prints the boolean result, This comes off as true because a is not equal to b

a = 5 # Assigns the integer value 5 to the variable a

b = 4 # Assigns the integer value 4 to the variable b

print(a < 8 and b < 5) #This is a logical operator, basically it is a and operator, basically it is the same as a < 8 and b < 5, Checks if a is less than 8 AND b is less than 5, and prints the boolean result

print(a < 8 or b < 2) #This is a logical operator, basically it is a and operator, basically it is the same as a < 8 and b < 2, Checks if a is less than 8 OR b is less than 2, and prints the boolean result

x = True # Assigns the boolean value True to the variable x

print(x) # Prints the value of x

print(not x) # Prints the negation of x

x = not x # Negates the value of x and assigns it back to x


# Telusko: Number System Conversion in Python

print(bin(25))
 # Converts the integer 25 to a binary string, which is '0b11001'. Here's how the conversion works:

 # 1. Divide 25 by 2: Quotient = 12, Remainder = 1
 # 2. Divide 12 by 2: Quotient = 6, Remainder = 0
 # 3. Divide 6 by 2: Quotient = 3, Remainder = 0
 # 4. Divide 3 by 2: Quotient = 1, Remainder = 1
 # 5. Divide 1 by 2: Quotient = 0, Remainder = 1

 # Make sure to read the remainders in reverse order to see the binary representation: 11001.  The '0b' prefix indicates that it's a binary string. So, bin(25) returns '0b11001'.


print(oct(25))
 # Converts the integer 25 to an octal string, which is '0o31'. Here's how the conversion works:


print(hex(25)) # Converts the integer 25 to a hexadecimal string, which is '0x19'. Here's how the conversion works:



#Telusko: IDLE Previous Command History

 # Pressing the up arrow key in the IDLE shell(Terminal) and it will show the previous command history, which is a list of commands that have been entered in the shell.



#Telusko : Python Bitwise Operators

#Bitwise operators include complement (~), and(&), or(|), xor(^), left shift(<<), right shift(>>)


#Complement Operator (~):

print(~12)  #  This is the bitwise NOT operator. It flips all the bits.
     #  Think of it as -(x + 1). So ~12 becomes -(12 + 1) = -13.
     # The result is -13. This kind of operator will always be -(x + 1) because the bitwise NOT operator flips all the bits.


#And Operator (&):

print(12&13)  # This is the bitwise AND operator. It compares each bit of the first operand with the corresponding bit of the second operand. If both bits are 1, it sets the corresponding bit of the result to 1. Otherwise, it sets the corresponding bit of the result to 0.
print(25&30) # Evaluates to 24.  Bitwise AND compares bits: if both are 1, result is 1; otherwise, 0.
# In simpler terms: (25 + 30) - (difference between the two) in binary form to be precise.


#Or Operator (|):

print(12|13)  # This is the bitwise OR operator. It compares each bit of the first operand with the corresponding bit of the second operand. If either bit is 1, it sets the corresponding bit of the result to 1. Otherwise, it sets the corresponding bit of the result to 0. This is the opposite of the AND operator. It is used to combine two binary numbers. 


#Xor Operator (^):
# 0,0 - 1
# 0,1 - 0
# 1,0 - 1
# 1,1 - 0

print(12 ^ 13) # Equal to 1, because 12 XOR 13 = 01100 XOR 01101 = 00001
print(25 ^ 30) # Equal to 7, because 25 XOR 30 = 11001 XOR 11110 = 00111 which is equal to 7


#Left Shift Operator (<<):

# In left shift, the bits are shifted to the left and the empty spaces are filled with 0s. The leftmost bits are lost. They Shift only 2 bits to the left. So for example 1010 << 2 = 101000, this shows it increasing 2 zeros to the right of the original number, while shiflting the original number 2 bits to the left.
print(10 << 2) # Equal to 40, because 10 << 2 = 1010 << 2 = 101000, which is equal to 40


#Right Shift Operator (>>):

# In right shift, the bits are shifted to the right and the empty spaces are filled with 0s. The rightmost bits are lost. They Shift only 2 bits to the right. So for example 1010 >> 2 = 10, this shows it decreasing 2 zeros to the right of the original number, while shiflting the original number 2 bits to the right.


print(24 >> 2) # Equal to 6, because 24 >> 2 = 11000 >> 2 = 110, which is equal to 6


# Telusko : Import Math Functions

from math import sqrt # This is the square root function, which returns the square root of the number

import math # This is the math module, which contains a lot of mathematical functions

x = math.sqrt(25)
print(x)
print(type(x))
x = math.sqrt(15)
print(x)
print(type(x))
print(math.floor(2.9)) # This is the floor function, which rounds down to the nearest integer
print(type(math.floor(2.9)))

print(math.ceil(2.9)) # This is the ceiling function, which rounds up to the nearest integer
print(type(math.ceil(2.9)))
      
print(math.pow(3, 2)) # This is the power function, which raises the first number to the power of the second number
print(type(math.pow(3, 2)))
      
print(math.pi) # This is the value of pi, which is approximately 3.141592653589793
print(type(math.pi))
      
print(math.e) # This is the base of the natural logarithm, which is approximately 2.718281828459045
print(type(math.e))

import math as m # This is an alias for the math module, so you can use m instead of math
      
print(m.sqrt(25))
print(type(m.sqrt(25)))
print(sqrt(25))
print(type(sqrt(25)))
#Telusko : Working with Pycharm: Run, Debug, Breakpoints, Step Over, Step Into, Step Out, Resume Program, Stop Program, Restart Program, View Breakpoints, View Call Stack, View Variables, View Console, View Terminal, View Run, View Debug, View Project


print("Hello World") # This is a print statement, which prints the string "Hello World" to the console
print(type("Hello World"))

x = 5
print(type(x))
y = 6
print(type(y))
z = x + y
print(z)
print(type(z))

#Side point for start lining of code in replit(Not Telusko)
class Calc:
    def __init__(self, a, b):
        self.num1 = a
        self.num2 = b

    def add(self):
        return self.num1 + self.num2

    def mul(self):
        return self.num1 * self.num2


obj1 = Calc(5,6) # This is an object of the Calc class, which is an instance of the Calc class. It is created by calling the Calc class and passing in the two numbers 5 and 6.
print(type(obj1))
print(type(Calc))
print(obj1.add()) # This is a method call, which calls the add method of the Calc class, which returns the sum of the two numbers
print(type(obj1.add())) # This is a method call, which calls the add method of the Calc class, which returns the sum of the two numbers


# Telusko : Swap 2 Variables in Python

    # There are 3 ways to swap 2 variables in Python using the XOR operator, the tuple unpacking method, and the simple swap method.

a = 5 
b = 6

a = a ^ b # This is a bitwise XOR operator, which is used to swap two variables
b = a ^ b
a = a ^ b

a,b = b,a # This is a tuple unpacking, which is used to swap two variables

a = b  # This is a simple swap, which is used to swap two variables

b = a 

print(a)
print(b) 