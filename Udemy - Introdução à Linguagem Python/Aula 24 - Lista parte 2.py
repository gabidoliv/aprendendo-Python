lista = [124,345,72,46,6,7,3,1,7,0]

sorted(lista)#Função sorted requer que retorne um valor
print(lista)

#Para lista ser ordenada, precisa aplicar a função sorted a alguma variável
lista = sorted(lista)
print(lista)

lista.sort() #Método para ordenar lista. Alterar a lista original, não retorna nenhum valor

print(lista)

#Para ordenar lista de maneira decrescente 
lista.sort(reverse=True)
print(lista)

#Para inverter lista, último elemento passa para o primeiro etc. Nesse caso, retornará para ordem crescente
lista.reverse()
print(lista)

