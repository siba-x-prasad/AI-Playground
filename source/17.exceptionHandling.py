# Exception Handling
print("Exception handling using try and except")

try:
  print(x)
except:
  print("An exception occurred")

# use of try and except
print("use of try and except")
try:
  print(x)
except NameError:
  print("Variable x is not defined")
except:
  print("Something else went wrong")  

# Use of else in try and except
print("Use of else in try and except")
try:
  print("Hello")
except:
  print("Something went wrong")
else:
  print("Nothing went wrong")  

# use of ginally
print("Use of finaly")
try:
  print(x)
except:
  print("Something went wrong")
finally:
  print("The 'try except' is finished")  

# Raise an exception
print("raise an exception using raise keyword")
x = -1

if x < 0:
  raise Exception("Sorry, no numbers below zero")

