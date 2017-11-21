# Assigning string to a variable
a = "This is a string"
b = 'This is a string'
c = '''
This 
is 
a 
string'''
print(a)
print(b)
print(c)

my_sentence = 'My profession is automation testing. I love exploring new technologies'

print(my_sentence)

# 3rd Index
print(my_sentence[3])
# 3rd Index from last
print(my_sentence[-3])
# Prints substring stepping up 2nd character
# from 4th to 10th character
print(my_sentence[4:10:2])

# Length
print(my_sentence.__len__())

# String Cases
print(my_sentence.lower())
print(my_sentence.upper())
print(
    my_sentence.capitalize())  # Return a capitalized version of S, i.e. make the first character have upper case and the rest lower case.
print(my_sentence.swapcase())
print(my_sentence.title())

# Substring
print("\n \t " + my_sentence[0:30])
print("\n \t " + my_sentence[30:])

print("\n \t " + my_sentence[:2] + " goal")

splited = my_sentence.split(" ")
for i in splited:
    print("\t " + i)

# Python code to demonstrate working of
# strip(), lstrip() and rstrip()
str = "---geeksforgeeks---"

# using strip() to delete all '-'
print(" String after stripping all '-' is : ", end="")
print(str.strip('-'))

# using lstrip() to delete all trailing '-'
print(" String after stripping all leading '-' is : ", end="")
print(str.lstrip('-'))

# using rstrip() to delete all leading '-'
print(" String after stripping all trailing '-' is : ", end="")
print ( str.rstrip('-') )