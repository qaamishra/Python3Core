# Create a new dictionary
d = dict()  # or d = {}

# Add a key - value pairs to dictionary
d = {'pqr': 566, 'lmp': 455}
# print the whole dictionary
print(d)

# print only the keys
print(d.keys())

# print only values
print(d.values())

# iterate over dictionary
for i in d:
    print("%s  %d" % (i, d[i]))

# another method of iteration
for index, value in enumerate(d):
    print(index, value, d[value])

# check if key exist
print('pqr' in d)

# delete the key-value pair
del d['pqr']

# check again
print("pqr" in d)
