# Python if else
print("If elif else statement")
age = 31

if age <= 1 :
    print("Hello Baby")
elif age > 1 and age <= 10:
    print("Todler")
elif age > 10 and age < 23:
    print("Child")
else:
    print("Adult")            

# Match in Python = switch/ when clause
print("match")
day = 4
match day:
  case 1:
    print("Monday")
  case 2:
    print("Tuesday")
  case 3:
    print("Wednesday")
  case 4:
    print("Thursday")
  case 5:
    print("Friday")
  case 6:
    print("Saturday")
  case 7:
    print("Sunday")    

# While loop
print("While loop with brteak")
i = 1
while i < 6:
  print(i)
  if i == 3:
    break
  i += 1

## Continue statement - skip the item
print("Continue statement")
i = 0
while i < 6:
  i += 1
  if i == 3:
    continue
  print(i)

# else in shile loop
print("else in  while loop")
i = 1
while i < 6:
  print(i)
  i += 1
else:
  print("i is no longer less than 6")

# For loop and range
# Note that range(6) is not the values of 0 to 6, but the values 0 to 5.
# range(2, 6), which means values from 2 to 6 (but not including 6)
print("Range example")
for x in range(2, 6):
  print(x)

# Increment the sequence with 3 (default is 1):
print("Increment for loop")
for x in range(2, 30, 3):
  print(x)

# Else in for loop
for x in range(6):
  print(x)
else:
  print("Finally finished!")  

# Reversed Range
print("Reversed Range")
a = [10, 20, 30, 40, 50]
for b in reversed(a):
    print(b)

