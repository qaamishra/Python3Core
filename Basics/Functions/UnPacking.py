def fun(a, b, c, d):
    print(a, b, c, d)


# Driver Code
my_list = [1, 2, 3, 4]

# Unpacking list into four arguments
# function(my_list)  #This wont work
fun(*my_list)



# A sample program to demonstrate unpacking of
# dictionary items using **
def fun(a, b, c):
    print(a, b, c)

# A call with unpacking of dictionary
d = {'a': 2, 'b': 4, 'c': 10}
fun(**d)
