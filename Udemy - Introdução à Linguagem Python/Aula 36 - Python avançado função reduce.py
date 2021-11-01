''' função reduce 
Recebe uma lista e retorna um único valor para essa lista
Por exemplo: soma dos elementos dos valores de uma lista 
'''
from functools import reduce

#Definindo função soma
def soma(x,y):
    return x+y

lista = [1,3,5,10,20]

#reduce(função,lista)
soma = reduce(soma, lista)
print(soma)