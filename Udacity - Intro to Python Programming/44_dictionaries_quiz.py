animals = {'dogs': [20, 10, 15, 8, 32, 15], 
    'cats': [3,4,2,8,2,4], 
    'rabbits': [2, 3, 3], 
    'fish': [0.3, 0.5, 0.8, 0.3, 1]}

types1 = [type(k) for k in animals.keys()] # Busca os tipos de dados das chaves do dicionário animals
types2 = [type(v) for v in animals.values()] # Busca os tipos de dados dos valores do dicionário animals

print(types1)
print(types2)

print(animals['dogs'])
print(animals['dogs'][3])
# print(animals[3]) #KeyError: 3
print(animals['fish'])