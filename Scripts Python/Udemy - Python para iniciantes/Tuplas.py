tuplas=("tiago","python","udemy")
print(tuplas)
print(tuplas[0])
print(tuplas[1])
print(tuplas[2])


print(tuplas[0:2])#Mostra só 0 e 1
print(tuplas[0:1]) #=tuplas[0] com vírgula
print (tuplas[0])

print(len(tuplas))

print (tuplas+tuplas)

print (tuplas*5)

print(4 in tuplas) #False - Não tem 4 em tuplas

print("udemy" in tuplas)

lista=[1,4,"tiago"]
print(lista) #colchetes

tuplas2=tuple(lista)
print(tuplas2) #parênteses
