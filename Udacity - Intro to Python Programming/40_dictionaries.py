#Enquanto set coletam dados únicos, dicionários são mais flexíveis.
#Dicionários coletam pares de dados (chaves e valores)
#Diferente de listas que só podem ter chaves com inteiros, dicionários pode ter strings como chaves. 
#Em dicionários não é necessário ter todas as chaves do mesmo tipo de dado

elements = {"hydrogen": 1, "helium": 2, "carbon": 6}

print(elements)
print(elements["helium"])  # mostra o valor mapeado para "helium"
elements["lithium"] = 3  # insere "lithium" com valor 3 no dicionário
print(elements)

print("carbon in elements? ", "carbon" in elements)
print("dilithium in elements? ", elements.get("dilithium")) 
# Se é esperado que as buscas falhem às vezes, get pode ser uma escolha melhor que colchetes porque erros podem travar o programa (crash)

#Operadores de identidade (são diferentes de operadores de comparação)
n = elements.get("dilithium")
print("dilithium not in elements? ", n is None) # Verifica se n é igual a None - retorna True
print("dilithium in elements? ", n is not None) # Verifica se n não é igual a None - retorna False

'''
clear()	- Removes all the elements from the dictionary
copy()	- Returns a copy of the dictionary
fromkeys()	- Returns a dictionary with the specified keys and value
get()	- Returns the value of the specified key
items()	- Returns a list containing a tuple for each key value pair
keys()	- Returns a list containing the dictionary's keys
pop()	- Removes the element with the specified key
popitem()	- Removes the last inserted key-value pair
setdefault()	- Returns the value of the specified key. If the key does not exist: insert the key, with the specified value
update()	- Updates the dictionary with the specified key-value pairs
values()	- Returns a list of all the values in the dictionary
'''