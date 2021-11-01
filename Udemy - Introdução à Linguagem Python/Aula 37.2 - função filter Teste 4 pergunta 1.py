''' Dada a seguinte lista:

    lista = [1,2,3,4,5,6,7,8,9,10]
    lista2 = []


Modifique o código a seguir para que lista2 possua apenas números pares.

Qual linha de código pode ser usada para isso?
'''


lista = [1,2,3,4,5,6,7,8,9,10]
lista2 = []

def dobro(i):
    if i %2 == 0:
        return i 
lista2 = filter(dobro,lista)

lista2 = list(lista2)
print(lista2)
