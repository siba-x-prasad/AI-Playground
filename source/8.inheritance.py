# Inheritance
print("Class inheritance")

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def printDetails(self):
        print("name = "+self.name, "age = "+str(self.age))    

class Employee(Person):
    pass

x = Employee("siba", 36)
x.printDetails()

# override properties and use super
print("Override p[roperties, use super keyword")

class Student(Person):
    def __init__(self, name, age, lName):
        super().__init__(name, age)
        self.lName = lName
    def printDetails(self):
            print("name = "+self.name, "age = "+str(self.age), "lName = "+self.lName)    

x = Student("SibaPrasad", 36, "Mohanty")
x.printDetails()
