# Define a Dictionary, population,
# that provides information
# on the world's largest cities.
# The key is the name of a city
# (a string), and the associated
# value is its population in
# millions of people.

#   Key     |   Value
# Shanghai  |   17.8
# Istanbul  |   13.3
# Karachi   |   13.0
# Mumbai    |   12.5

population = {"Shanghai": 17.8, "Istanbul": 13.3, "Karachi": 13.0, "Mumbai": 12.5}

print(population)

#Busca no dicionário com o colchete - Não é recomendado por travar o programa ao buscar chave que não existe no dicionário

print(population["Karachi"])
print(population["Brazil"]) #KeyError