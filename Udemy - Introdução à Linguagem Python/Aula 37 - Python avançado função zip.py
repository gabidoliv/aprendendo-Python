''' função zip
Concatena os elementos de listas distintas para percorrer com laço for
'''
lista1 = [1,2,3,4,5]
lista2 = ["abacate", "bola", "cachorro", "dinheiro","elefante"]

#O primeiro item da lista 1 vai para numero e o primeiro da lista 2 vai pra nome e assim, sucessivamente
for numero, nome in zip(lista1, lista2):
    print(numero,nome)