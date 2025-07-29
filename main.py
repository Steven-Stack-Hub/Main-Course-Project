name = "Beaux"
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

# User Input
age = input("What is your age? ")
print("Your age is " + age)

#Control Statement 
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

#Lists
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

#Sorting Lists
items = ['Roger', 'Zion', 'Flavio', 'flavio', 'Roger']
items.sort() # This is a function to sort a list in its order and automatically makes the first letter uppercase and the rest lowercase. It puts 'flavio' at the end because everything else is uppercase and it is lowercase, and is also aware of the alphabetical order.
itemscopy = items[:] # This is a function to copy a list
print(items)
items.sort(key=str.lower) # This is a function to sort a list in alphabetical order ignoring uppercase letters and lowercase letters and numbers 
print(items)
print(itemscopy) # This is a copy of the origiinal Sorted List with undercase 'flavio' at the end

# Tuples
names = ("Roger", "Syd", "Flavio")  #
print(names)
names[-1]
names.index("Roger") # This is a function to find the index of an item in a tuple, basically the position of the item in the tuple

len(names)

print("Roger" in names)
print(sorted(names)) # This is a function to sort a tuple in alphabetical order
newTuple = names + ("Tina", "Rufus") # This is a function to add a tuple to another tuple

print(newTuple)

# Dictionaries
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
enumerate # This is a function to enumerate a dictionary, which is a list of tuples
#Enumerating Lists
letters = ["a", "b", "c", "d"]
for index, letter in enumerate(letters):
    print(index, letter)
print(list(enumerate(dog))) # This is a function to print the list of tuples of a dictionary
