# Python Lambda
print("Single argument lambda")
x = lambda a: a*a
print("square of 5 is "+str(x(5)))

print("Multiple argument lambda 1")
x = lambda a,b: a+b
print("sum of 5 and 6 is "+str(x(5, 6)))

print("Multiple argument lambda 2")
x = lambda a,b,c: a*b*c
print("mul of 5,6, is "+str(x(5, 6,7)))


def myfunc(n):
  return lambda a : a * n

mydoubler = myfunc(2)
mytripler = myfunc(3)

print(mydoubler(11))
print(mytripler(11))