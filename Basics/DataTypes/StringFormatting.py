# The formatting using % is similar to that of ‘printf’ in C programming language.
# %d – integer
# %f – float
# %s – string
# %x – hexadecimal
# %o – octal


variable = '15'
string = "Variable as string = %s" % (variable)
print(string)

# Convert the variable to integer
variable = int(variable)
string = ("Variable as integer = %d" % (variable))
print(string)

print ("Variable as float = %f" % (variable))
