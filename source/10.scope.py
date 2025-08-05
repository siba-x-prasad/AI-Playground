# Scope
print("Python variable scope")
# A variable is only available from inside the region it is created. This is called scope.
def myfunc():
  x = 300
  print(x)

myfunc()
# The local variable can be accessed from a function within the function:
print("The local variable can be accessed from a function within the function:")
def myfunc():
  x = 300
  def myinnerfunc():
    print(x)
  myinnerfunc()

myfunc()


# Global Scope
print("Global Scope")
x = 300

def myfunc():
  print(x)

myfunc()

print(x)
# global keyword
print("global keyword")
def myfunc():
  global x
  x = 300

myfunc()

print(x)

# Nonlocal Keyword
print("Nonlocal Keyword")
# The nonlocal keyword is used to work with variables inside nested functions.
# The nonlocal keyword makes the variable belong to the outer function.

def myfunc1():
  x = "Jane"
  def myfunc2():
    nonlocal x
    x = "hello"
  myfunc2()
  return x

print(myfunc1())


