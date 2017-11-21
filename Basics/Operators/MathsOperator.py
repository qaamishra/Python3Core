import operator

a = 5
b = 4

print("Add : ", end="")
print(operator.add(a, b))

print("Sub : ", end="")
print(operator.sub(a, b))

print("Mul : ", end="")
print(operator.mul(a, b))

print("truediv : ", end="")
print(operator.truediv(a, b))

print("floordiv : ", end="")
print(operator.floordiv(a, b))

print("pow : ", end="")
print(operator.pow(a, b))

print("mod : ", end="")
print(operator.mod(a, b))

print("less than ,if a is less than b : ", end="")
print(operator.lt(a, b))

print("less than or equal ,if a is less than or equal b : ", end="")
print(operator.le(a, b))

print("equal ,if a is equal to b : ", end="")
print(operator.eq(a, b))

print("gt : ", end="")
print(operator.gt(a, b))

print("ge : ", end="")
print(operator.ge(a, b))

print("ne : ", end="")
print(operator.ne(a, b))
