from functools import *


# A normal function
def add(a, b, c):
    return 100 * a + 10 * b + c

print(add(3,2,1))
#Partial functions allow us to fix a certain number of arguments of a function and generate a new function.
# A partial function with b = 1 and c = 2
add_part = partial(add, b=2, c=1)

# Calling partial function
print(add_part(3))
