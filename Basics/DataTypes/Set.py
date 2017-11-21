normal_set = set(["a", "b", "c"])
normal_set.add("a")#adding again samething will not add
print("Normal Set",end="     ")
print(normal_set)

# A frozen set
frozen_set = frozenset(["e", "f", "g"])
print("Frozen Set",end="   ")
print(frozen_set)
#frozen_set.add("h")


normal_set.add("New")
print(normal_set)
unioinOfSet=normal_set.union(frozen_set)
print(unioinOfSet)