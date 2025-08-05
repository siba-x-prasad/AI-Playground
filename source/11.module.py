# Modules
print("Modules")

import moduleExample

moduleExample.greeting("siba")

# Rename a module
import moduleExample as abcd
abcd.greeting("sp")

# Builtin modules
import platform

x = platform.system()
print(x)

# dir()
# There is a built-in function to list all the function names (or variable names) in a module. The dir() function:
import platform

x = dir(platform)
print(x)


