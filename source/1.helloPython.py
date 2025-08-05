print("Welcome to Python")

# Single line command

"""
Multi line command
"""

# Datatypes
"""
Integer
Float
String
Lists
Tuple
Dictionary
Boolean
"""

# Integer and Float
age = 36
height = 5.8

# String
name = "sibaprasad"
greeting = "Hello "+name

# Lists
numbers = [1,2,3,4,5]
names = ["siba", "prasad","shrinaya", "swayam"]
coordinates = (10, 20)

# Dictionary
person = {"name": "sibaprasad", "age": 36}

# Boolean

is_Student = False


# Define variables
integer_var = 10
float_var = 3.14
string_var = "AI"
list_var = [1, 2 , 3]
tuple_var = (4, 5, 6)
dictionary_var = {"name": "sibaprasad", "age": 36}
boolean_Var = True

# Print and Manipulate 
print("integer_var", integer_var)
print("float_var", float_var)
print("string_var", string_var)
print("list_var", list_var)
print("tuple_var", tuple_var)
print("dictionary_var", dictionary_var)
print("boolean_Var", boolean_Var)

# Many values to multiple variables
x, y, z = "Orange", "Banana", "Cherry"
print("x", x)
print("y", y)
print("z", z)
# One value to multiple variable
x = y = z = "Orange"
print("x", x)
print("y", y)
print("z", z)
# Unpack a Collection
fruits = ["apple", "banana", "cherry"]
x, y, z = fruits
print(x)
print(y)
print(z)

# Output variables
x = "Python is awesome"
print(x)

x = "Python"
y = "is"
z = "awesome"
print(x, y, z)
print(x + y + z)

# Global Variables
x = "awesome"

def myfunc():
  print("Python is " + x)

myfunc()

x = "awesome"

def myfund():
  x = "fantastic"
  print("Python is " + x)

myfund()

print("Python is " + x)
