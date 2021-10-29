minha_lista = ["abacaxi", "melancia","abacate"]
minha_lista_2 = [1,2,3,4,5]
minha_lista_3 = ["abacaxi", 2, 9.89, True]
minha_lista_4 = [] #Criar lista em branco

print (minha_lista_4)

minha_lista.append("limão") #Adicionar elementos à lista - Método append
minha_lista_4.append(57)

print(minha_lista)
print(minha_lista_2)
print (minha_lista_3)
print(minha_lista_4)

#Indicando valor de índice para mostrar na tela elemento a elemento
print(minha_lista[2])

#Navegar pelos elementos da lista usando laço for

for item in minha_lista: 
    print(item)

#Verificar tamanho da lista

tamanho = len(minha_lista)
print(tamanho)

#Verificar se um elemento pertence a uma lista utilizando palavra reservada in
if 7 in minha_lista_2:
    print("7 está na lista")
if 3 in minha_lista_2:
    print("3 está na lista")

#Remover elementos da lista utilizando palavra reservada del
del minha_lista[2:]
print(minha_lista)

#Apagar a lista inteira
del minha_lista[:]
print(minha_lista)