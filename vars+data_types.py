# variables - a reference (a name), a section of memory.
# protected - cant be altered unless called by name. Memory reserved. 

#age = 10
#x = 30

# naming convention - names should be descriptive, lowercase, never start with a number
# pep-8 style guide
# be consistant

# Var = 12 # avoid capital
# 1var = 12 # cant start with a number
# VAR = 20 constants - the data shouldnt be changed. 
# print = 1 # avoid python keywords

# person_one_age = 10 # snake case
# personOneAge = 10 #camel case 

#x = 10
#age = 10

# built-in functions

#print('print to standard output')
#type(show our data-type)
#input(allows input from standard input)
#class(build a class - oop)

# data types

#x = 10 # integer - whole number
#y = '10' # string - words, paragraphs etc
#z = False # Bool - true or force, 0 or 1, something or nothing)
#v = 10.25 # float - decimal int. 

# print(type(y))

#name = input("what is your name? ") # input defaults to a string.
#age = int(input("what is your age? ")) 

#print("your name is" + name)
#print("your name is", name)
#print(f"your name is {name}, your {age} years old!")

#name = "rex"
#age = 3
#bark = True
#meow = False

#print("statement: ", name, "barks:", bark)

# escape chars

# \\ backslash, \" name \", \n - new line, \t - tab, \u unicode, \U extended unicode

# print("person 1: \tHey how are you?\nPerson 2: \tGood thanks \U0001F604")

# string methods

#print("hELLO WoRlD".lower())
#print("hello world".upper())

#print("hello world".replace("world", "class"))
#print("hello world".count("o"))
print("hello world".split(","))

# BODMAS

# brackets
# order Of
# division
# multiplication
# addition
# subtraction

# + - / *
#power of **
# floor division // 10//3 = 3
#modulo % 10%3 = 1 

length = int(input("enter the length of the rectangle: ")) 
width = int(input("enter the width of rectangle: "))

perimeter = 2 * (length + width)

print("perimeter: ", perimeter)















