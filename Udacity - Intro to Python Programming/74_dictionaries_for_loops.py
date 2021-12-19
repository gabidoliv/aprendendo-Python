# Iterar em dicionários usando for na forma for n in algum_dicio vai dar acesso às chaves desse dicionário
# O exemplo abaixo é um caso de iterar tanto nas chaves quanto nos valores do dicionário
# Dicionario com chaves = nome de atores e valores = personagens interpretados por esses atores

cast = {
    "Jerry Seinfeld":"Jerry Seinfeld",
    "Julia Louis-Dreyfus":"Elaine Benes",
    "Jason Alexander":"George Costanza",
    "Michael Richards":"Cosmo Kramer"
}
# Laço for fornece apenas as chaves
print("Iterando chaves: ")
for key in cast: 
    print(key) 

# Bulti-in: Método items - fornece chaves e valores do dicionário
print("Iterando chaves e valores:")
for key, value in cast.items():
    print("Ator: {}\t\tPapel:{}".format(key,value))
# items é um método que retorna tuplas de chaves e valores em pares