# Declaring a list
L = [1, "a", "string", 1 + 2]
print(L)
print("=========")
L.append(6)
print(L)
print("=========")
# deletes last element
L.pop()
print(L)
print("=========")
L.pop(0)
print(L)

print("=========")
print(L[1])

print("=========")
# L.sort() TypeError: '<' not supported between instances of 'int' and 'str'
# print(L)

print("=========")
myNames = ["Test", "QA", "Automation", "Python"]
myNames.sort()
print(myNames)

print("=========")
myInts = [10, 25, 99, 40]
myInts.sort(reverse=True)
print(myInts)

print("=========")
myInts.reverse()
print(myInts)

print("=========")
myNames = ["Test", "QA", "Automation", "Python"]
myNames.insert(1,"We")
print(myNames)
print(myNames[2:myNames.__len__()-1]) #Print from index 2 to myNames length -1