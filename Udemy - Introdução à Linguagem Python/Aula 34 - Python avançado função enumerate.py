# função enumerate

lista = ["abacate", "bola","cachorro"]

#Imprimir os valores por linha
for i in lista:
    print(i)

#Imprimir a posição e os valores por linha
for i in range(len(lista)):
    print(i, lista[i])

#Forma "pythônica"

for i, nome in enumerate(lista): #i para índice/posição e nome para o valor
    print(i, nome)