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
def is_adult(age):
    if age > 18:
        return True
    else:
        return False  # This is a slower way to do it


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

items.pop() # This is a function to remove the last item from the list

print(id(items)) # This is a function to print the id of the object, which is the memory address of the object.

age = age + 1

#Loops: Loops are used to iterate over a sequence (that is either a list, a tuple, a dictionary, a set, or a string).

condition = True
while condition == True:
    print("The condition is True")
    condition = False

count = 0
while count < 10:
    print("The condition is True")
    count = count + 1

print("After the loop")

items = [1, 2, 3, 4]
for item in items:
    print(item)

for item in range(15):
    print(item)

items = ["Beau", "Roger", "Syd"]
for index, item in enumerate(items): # This is a function to iterate through a list and print the index and the item, basically the position of the item in the list and the item itself.
    print(index, item)

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
        print("Walking...")


class Dog(Animal):
    def __init__(self, name, age): # This is a constructor, which is a special method that is called when an object is created. It is used to initialize the object.
        self.name = name # This is a property of the object, which is a variable that is associated with the object.
        self.age = age # This is a property of the object, which is a variable that is associated with the object.
        
    def bark(self): # This is a method to print a string, basically a function that is defined inside a class.
        print("Woof!")

roger = Dog("Roger", 8) # This is an object of the Dog class, which is an instance of the Dog class. It is created by calling the Dog class and passing in the name and age of the dog.

print(roger.name) # This is a function to print the name of the object, which is the name of the dog.
roger.bark()
roger.walk()
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

multiply = lambda a, b: a * b

print(multiply(2, 4))

#Map(), Filter(), Reduce() : Map, filter, and reduce are functions that are used to apply a function to a sequence of elements.


#Map(): Map is a function that applies a function to a sequence of elements. It returns a new list with the results of applying the function to each element in the sequence.
numbers = [1, 2, 3, 4, 5]

def double(a): # This is a function to double a number, which is a lambda function that takes a number and returns the number multiplied by 2.
    return a * 2
result = map(double, numbers)
print(list(result))

#Map(): Map is a function that applies a function to a sequence of elements. It returns a new list with the results of applying the function to each element in the sequence.









































    #Telusko
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

a = 10 # Assigns the integer value 10 to the variable a

b = a # Assigns the value of a (which is 10) to the variable b

print(id(a)) # Prints the memory address of the variable a

print(id(b)) # Prints the memory address of the variable b

print(id(10)) # Prints the memory address of the integer literal 10

k = 10 # Assigns the integer value 10 to the variable k

print(id(k)) # Prints the memory address of the variable k

a = 9 # Assigns the integer value 9 to the variable a

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

print(a != b) #This is a comparison operator, basically it is a not equal to operator, basically it is the same as a != b, Checks if a is not equal to b and prints the boolean result

a = 5 # Assigns the integer value 5 to the variable a

b = 4 # Assigns the integer value 4 to the variable b

print(a < 8 and b < 5) #This is a logical operator, basically it is a and operator, basically it is the same as a < 8 and b < 5, Checks if a is less than 8 AND b is less than 5, and prints the boolean result

print(a < 8 or b < 2) #This is a logical operator, basically it is a and operator, basically it is the same as a < 8 and b < 2, Checks if a is less than 8 OR b is less than 2, and prints the boolean result

x = True # Assigns the boolean value True to the variable x

print(x) # Prints the value of x

print(not x) # Prints the negation of x

x = not x # Negates the value of x and assigns it back to x