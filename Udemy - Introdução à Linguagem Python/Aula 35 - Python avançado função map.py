# função map

#Aplica função a todos os elementos de uma lista

def dobro (x):
    return x*2

valor = 2 
print(dobro(valor))

#Aplicando a vários valores

valores = [1,2,3,4,5]
print(dobro(valores)) #A lista será duplicada de tamanho, concatenando

#map(função, lista)

print(map(dobro, valores)) #Mostra objeto e não retorna a lista com valor dobrado, precisa criar variável

valor_dobrado = map(dobro, valores)

#Laço for para mostrar cada elemento multiplicado por 2
'''
for v in valor_dobrado:
    print(v)
'''

#Outra forma = converter em lista

valor_dobrado = list(valor_dobrado)
print(valor_dobrado)