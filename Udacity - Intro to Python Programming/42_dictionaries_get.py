elements = {"hydrogen": 1, "helium": 2, "carbon": 6}

# print(elements['dilithium']) # KeyError: 'dilithium'
print(elements.get('dilithium')) # None

print(elements.get('kryptonite', 'There\'s no such element!')) #There's no such element

print(elements.get('hydrogen', 'There\'s no such element!')) #1