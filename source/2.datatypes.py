# Text Type:	str
# Numeric Types:	int, float, complex
# Sequence Types:	list, tuple, range
# Mapping Type:	dict
# Set Types:	set, frozenset
# Boolean Type:	bool
# Binary Types:	bytes, bytearray, memoryview
# None Type:	NoneType

# Getting the Data Type
print("Getting the Data Type")
x = 5
print(type(x))


x = "Hello World"		
x = 20		
x = 20.5		
x = 1j		
x = ["apple", "banana", "cherry"]		
x = ("apple", "banana", "cherry")	
x = range(6)		
x = {"name" : "John", "age" : 36}		
x = {"apple", "banana", "cherry"}		
x = frozenset({"apple", "banana", "cherry"})		
x = True		
x = b"Hello"		
x = bytearray(5)		
x = memoryview(bytes(5))		
x = None		

# Setting the Specific Data Type
print("Setting the Specific Data Type")

x = str("Hello World")
x = int(20)		
x = float(20.5)		
x = complex(1j)		
x = list(("apple", "banana", "cherry"))		
x = tuple(("apple", "banana", "cherry"))		
x = range(6)		
x = dict(name="John", age=36)		
x = set(("apple", "banana", "cherry"))		
x = frozenset(("apple", "banana", "cherry"))		
x = bool(5)		
x = bytes(5)		
x = bytearray(5)		
x = memoryview(bytes(5))	


# Python casting
print("ython casting")

x = int(1)   # x will be 1
y = int(2.8) # y will be 2
z = int("3") # z will be 3

x = float(1)     # x will be 1.0
y = float(2.8)   # y will be 2.8
z = float("3")   # z will be 3.0
w = float("4.2") # w will be 4.2

x = str("s1") # x will be 's1'
y = str(2)    # y will be '2'
z = str(3.0)  # z will be '3.0'

