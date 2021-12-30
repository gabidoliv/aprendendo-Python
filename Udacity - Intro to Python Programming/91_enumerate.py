# Função que retorna um iterador de tuplas contendo índices e valores de uma lista
# enumerate é usado geralmente quando você quer, durante um loop, o index junto com cada elemento de um iterável

letters = ['a', 'b', 'c', 'd', 'e']
for i, letter in enumerate(letters):
    print(i, letter)