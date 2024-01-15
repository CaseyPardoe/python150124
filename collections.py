# different ways of storing dat 
# lists - ordered, mutable, collection of values [a, b, c.....]
# dictionaries - unordered, mutable, collection of key-pair values {"key": ["value", "value1"], key...}
# tuples - ordered, immutable, collection of values (a, b, c) or a, 1-, [a,b,e]
# sets - unordered, mutable, collection of unique values {value1, value2....}

# lists are stored in a variable = []

#colours = ["blue", "green", "red", "yellow"] 

#print(colours)

# referencing elements in a list by their index position
# starts [0] and also [-1]

#print(colours[0])
#print(colours[3])
#print(colours[-4])

# slicing create a sub-list up to but not including the 2nd number

#print(colours[0:2])
#print(colours[1:]) # no 2nd number slices till the end of the list 

# altering list - use index position, need a value, delete with del

#food = ["bread", "cheese", "pasta", "apple"]

#print(food)
#food[0] = "rice"
#print(food)

#del food[1]
#print(food)

# check if an item was in a list

#print("pasta" in food)
#print("orange" in food)

# nested list

#numbers = [1, 2, 3, 4]
#letters = ["a", "b", "c", "d"]

#combined = [numbers, letters]

#print(combined[0][1], combined[1][1])

# multiple data types

#my_list = ["red", 5, ["green", "apple"], 10.5]

#print(my_list)
#print(my_list[2][0])
#print(my_list[0])

# List methods

# append

#my_fruits = ["apple", "orange", "kiwi"]


#my_fruits.append("pear")
#print(my_fruits)

# remove

#my_fruits.remove("apple")
#print(my_fruits)

# insert

#my_fruits.insert(0, "mango")
#my_fruits.insert(0, "grape")
#print(my_fruits)

# extend  - with a list

#my_fruits.extend(["grapes", "melon"])
#print(my_fruits)

# index (fining index position)

#print(my_fruits.index("mango"))

# reverseing + sorting 

#my_fruits.reverse()
#print(my_fruits)


#my_fruits.sort()
#print(my_fruits)

#my_fruits.sort(key=len)
#print(my_fruits)


# join

#x = ", ".join(my_fruits)
#print(x)
#print(type(x))


# Dictionaries {} key:value pairs
# similar to list but no indexing
# keys have to be unique, value dont

drinks = {"fizzy": "sprite", "still": "water", "juice":"orange", "alcoholic":"wine"}

print(drinks)
# direct access
print(drinks["still"]) # can only query with the key not the value

# add to dictionary

drinks["non-alchohlic"] = "water"
print(drinks)

# overwrite

drinks["non-alchohlic"] = "squash"
print(drinks)

# returning values and keys and both

print(drinks.values())
print(drinks.keys())
print(drinks.items())

print("water" in drinks.values())
print("still" in drinks)

# get method

print(drinks.get("still"))
print(drinks.get("stillie", "not-found"))

# update method

drinks.update({"sugery": "cola"})
print(drinks)
drinks.update({"more sugery": "red bull"})
print(drinks)

# pop method - delete and retrieve

print(drinks.pop("non-alchohlic"))
print(drinks.pop("non-alchohlic", "not-found"))
print(drinks)

# exerise

# make a dictionary of books, with 3 authors and multiple books per author.
# ~Use an input asking for an author name
# print back as a string a list of the books by that author.
# use the .join()

dict = {"author1": ["book1", "book2"], "author2" : [] .......}





























