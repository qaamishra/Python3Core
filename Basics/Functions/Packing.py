def mySum(*args):
    sum = 0
    for i in range(0, len(args)):
        sum = sum + args[i]
    return sum


# Driver code
#Here we do not  know how many arguments we may pass to function
print(mySum(1, 2, 3, 4, 5))
print(mySum(10, 20))