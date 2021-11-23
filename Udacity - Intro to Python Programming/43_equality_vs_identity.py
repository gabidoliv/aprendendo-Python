a = [1, 2, 3]
b = a
c = [1, 2, 3]

print(a == b) # True
print(a is b) # True
print(a == c) # True
print(a is c) # False - a e c apontam pra objetos diferentes, não formam identidade