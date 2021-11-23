#Enquanto set coletam dados únicos, dicionários são mais flexíveis.
#Dicionários coletam pares de dados (chaves e valores)
#Diferente de listas que só podem ter chaves com inteiros, dicionários pode ter strings como chaves. 
#Em dicionários não é necessário ter todas as chaves do mesmo tipo de dado

elements = {"hydrogen": 1, "helium": 2, "carbon": 6}

print(elements)
print(elements["helium"])  # mostra o valor mapeado para "helium"
elements["lithium"] = 3  # insere "lithium" com valor 3 no dicionário
print(elements)

print("carbon" in elements)
print(elements.get("dilithium")) 
# Se é esperado que as buscas falhem às vezes, get pode ser uma escolha melhor que colchetes porque erros podem travar o programa (crash)

#Operadores de identidade (são diferentes de operadores de comparação)
n = elements.get("dilithium")
print(n is None)
print(n is not None)