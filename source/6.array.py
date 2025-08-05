# Array
fruits = ["apple", "banana", "mango", "Orange", "grapes"]

print("Array")
print("Length is len(array) = "+str(len(fruits)))
def printFruits():
    for fruit in fruits:
     print(fruit)
printFruits()
# add items to array using apend
fruits.append("Avacado") 
print("fruits after apend avacado")
printFruits()

fruits.pop(1) 
print("fruits after remove using pop(1)")
printFruits()

fruits.remove("Avacado") 
print("fruits after remove avacado")
printFruits()

# append()	Adds an element at the end of the list
# clear()	Removes all the elements from the list
# copy()	Returns a copy of the list
# count()	Returns the number of elements with the specified value
# extend()	Add the elements of a list (or any iterable), to the end of the current list
# index()	Returns the index of the first element with the specified value
# insert()	Adds an element at the specified position
# pop()	Removes the element at the specified position
# remove()	Removes the first item with the specified value
# reverse()	Reverses the order of the list
# sort()	Sorts the list

