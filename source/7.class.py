# Class
class myClass1:
    name = "Myfirst class in python"

a = myClass1()
print(a.name)

class MyClass2:
    def __init__(self, fname, lname, age):
        self.fname = fname
        self.lname = lname
        self.age = age
    def printProperties(self):
        print("fname = "+self.fname, "lname = "+self.lname, "age = "+str(self.age))    

x = MyClass2("siba", "mohanty", 36)
x.printProperties()

# modify the object properties
print("Print the object properties")
x.age = 123
x.printProperties()

# delete the properties
print("Delete the properties")
del x.age
# x.printProperties() - it will delete the property
# delete object
del x

# The pass Statement
print("The pass Statement")
class Person:
  pass




