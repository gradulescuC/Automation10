# A. PRINT FUNCTION
from math import floor, ceil  # here we import an external library

print("Hello world!") #print is a python instruction that help us display text on the screen
print("Mc. \"Donalds") # the \ sign can be used as what we call an escape mechanism
                            # the escape mechanism makes a character be considered text to be displayed on the screen instead of part of the code
print ("Mc 'Donalds'") # we can also make use of a mixture of quotes and double quotes in order to not use the escape character in this case

#  ---------------------------------------------------------------------------------------------------------------------
# B. VARIABLES

""" 
1. A variable is a reserved space in the system memory that can store information that can be changed over time
2. A variable must be defined by a name that will represent the name of the memory where the variable is defined
3. Variables will be created only after assigning them a value to be stored in the memory that is reserved
4. Rules for naming a variable
- variable names must not contain spaces
- variable names must not be named with reserved words (for example we cannot name a variable as print)
- variable names must be unique
- variable names must not start with a number (they can contain numbers as long as they do not start with one)
- usually variables follow the format snake_case or camelCase (usually snake_case)
- variable names should start with lowercase
- variables are case sensitive
 """

# Declaring and initializing variable
modelMasina = 'v60'

# changing the data type of a variable
modelMasina = 60

# one line initialization
x,y,z, = 'Banana','Mar','Portocala'
print(z,y)

# C. CONSTANTS
"""
- Constants are memory spaces that should not change their value
- In python the concept of constant does not exist, so when we want to defined constants, as a convention we will use capitals as a name
"""

# D. IN BUILT FUNCTIONS
incercare = "test"
nr = 13.456789
print(len(incercare)) #The len function calculates the number of characters the value in a specific variable has. In this case it will print 4
print(round(nr)) #
print(floor(nr))
print(ceil(nr))
print(type(nr)) # the type function extracts the data type of a specific variable

# E. DATA TYPES
"""
A data type is an information that informs the system about the type of information we can store in a specific variable

The most used data types in python:
- int (short for integer) -> Can store only integer values (1,2,9,99,167834534 etc)
- float -> Can store decimal numbers (16 decimal points)
- bool (short for boolean) -> Can store true or false values  (with first letter in capital letter)
- string -> Can store text
"""

age = 3
quantity = 24.5
isActive = True
customer_name = "john"

float_nr = 123456789.1234567890123456
print(float_nr)

# We cannot concatenate two variables having two data types, but we have workarounds for this
name = 'Michael'
age = 33
# print("My name is" + name + "and I have" + age + "years old") - this will return error because we cannot concatenate string and numeric data types
print("My name is" + name + "and I have" + str(age) + "years old") # this will work
print("my name is {0} and I am {1} years old ".format(name,age))  #this is harder to read and it is not recommended.
print(f"My name is {name} and I have {age} years old") # this is the best option (the most optimal)
                            #f forces the variables between brackets to be treated as strings
                            #f is short for - format string -
# F. TYPE CASTING
# type casting means changing the data type of the value in a specific variable
type_casting_example = 33
print('---------------------------')
print(type(type_casting_example))
print(type(float(type_casting_example)))
print(type(str(type_casting_example)))
type_casting_example_1 = float(type_casting_example)
print(type(type_casting_example), type(type_casting_example_1))

# G. KEYBOARD INPUT
"""
- it help us extract values from the keyboard (interactive values)
- by default the inserted data has the type int
- we can save the values in variables and use them afterwards
"""
a = 3
b = int((input("alege un numar "))) #we cast to int in order to be able to add the two numbers, otherwise we will get an error
print(a+b)
# name,age,gender = input("enter the name|age|gender").split('|') # in this case when we insert we separate values by |
name,age,gender = input("enter the name|age|gender ").split() # default separator is space
print(name,age,gender)

# H.

# I. STRING (index, len, slicing, metode)
"""
- each character in a string has an index identifying its position
- the first index is 0 
- we can slice a string by using the following sintax: my_str[start_pos,end_pos,step]
"""

# a) The following are examples of string slicing
sentence = "My name is python and i am a snakes"
print(len(sentence))
print(sentence[0])
print(sentence[0:3]) # it prints the characters in the position 0,1,2
print(sentence[::-1]) # it crosses the string in reverese
print(sentence.upper()) # prints the string with capital letters
print(sentence[-1]) # prints the last character in the string
print(sentence[-3]) # prints the third character from the end
print(sentence[0:10:2]) # prints the characters from start to end with a step of 2, meaning it will jump every other character
part1 = sentence[0] # we save the first character

print('-----------------------------------------------------------------------------------------------------------------')

# b) string methods
print(sentence.count('a')) # counts how many times do we have the character a in the string
print(sentence.upper())
print(sentence.replace('i','y'))
# https://stackoverflow.com/questions/509211/understanding-slice-notation/46614773 -> More info about slice notation
myStr = 'Azi e miercuri'
# I want to go through it until the one before the last character
# I want to find out the last index
last_index = len(myStr)-1 # we add -1 because the index starts from 0
print(last_index) # we check the last index
print(f"The last letter in \"{myStr}\" is \"{myStr[last_index]}\"")
print(myStr[0:last_index])
part2 = sentence[1:].replace('s','$')
print(part1,part2)
sentence = "Test abc"
print(sentence.replace("Test","nothing"))
# c) string index
print(myStr[0])
print(myStr[10])
print(myStr[last_index])