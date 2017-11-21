# below list contains square of all odd numbers from range 1 to 10
odd_square = [x ** 2 for x in range(1, 11) if x % 2 == 1]
print(odd_square)

# x ** 2 is output expression,
# range (1, 11)  is input sequence,
# x is variable and
#  if x % 2 == 1 is predicate part.


# list which extracts number
string = "my phone number is : 11122 !!"
print("\nExtracted digits")
numbers = [x for x in string if x.isdigit()]
print(numbers)


#https://www.python-course.eu/python3_lambda.php