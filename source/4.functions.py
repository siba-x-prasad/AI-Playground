# Function
print("Function")

def myFunction():
    print("This is my first python function")
    print("This is my first python function 2nd statement")

myFunction()

print("Function with arguments")

def my_function(fname):
  print(fname + " Refsnes")

my_function("Emil")
my_function("Tobias")
my_function("Linus")

# Arbitrary Arguments, *args
print("Arbitrary Arguments, *args")
def my_function(*kids):
  print("The youngest child is " + kids[2])

my_function("Emil", "Tobias", "Linus")

# keyword argument function
print("Keyword argument functions")

def myKeywordArgumentFunction(argument1, argument2, argument3):
   print("argument1"+argument1, "argument2"+argument2, "argument3"+argument3)

myKeywordArgumentFunction(argument1= "Hello", argument2="Python", argument3="tutorial")

# Arbitrary Keyword Arguments, **kwargs - receive dictionary of arguments
def arbitraryKeywordArgumentFunction(**personDictionary):
   print("firstname = "+personDictionary["fName"], "lastLastName = "+personDictionary["lName"], "Age = "+str(personDictionary["age"]))

arbitraryKeywordArgumentFunction(fName = "Siba", lName = "Mohanty", age= 36)

# Default Parameter Value
print("Default Parameter Value")

def defaultParameterFunction(name = "sibaprasad"):
   print("Hello "+name)

defaultParameterFunction()
defaultParameterFunction("Swayam")
defaultParameterFunction("siya")   

# Passing list as argument
print("Passing list as argument")
def my_function(food):
  for x in food:
    print(x)

fruits = ["apple", "banana", "cherry"]
my_function(fruits)

# return function
print("Function return values")
def squareFun(item):
   return item * item

print("Square of 5 is "+str(squareFun(5)))
print("Square of 6 is "+str(squareFun(6)))

# Positional-Only Arguments
# You can specify that a function can have ONLY positional arguments, or ONLY keyword arguments.
# To specify that a function can have only positional arguments, add , / after the arguments:
def positionalOnlyfunction(x, /):
  positionalOnlyfunction(x)

my_function(3)

