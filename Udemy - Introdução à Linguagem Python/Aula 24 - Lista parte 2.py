lista = [124,345,72,46,6,7,3,1,7,0]

sorted(lista)#Função sorted requer que retorne um valor
print("Essa lista não está ordenada com sorted: ", lista)

#Para lista ser ordenada, precisa aplicar a função sorted a alguma variável
lista2 = sorted(lista)
print("Essa lista está ordenada com sorted: ", lista2)
print("Essa lista é a original: ", lista)

lista.sort() #Método para ordenar lista. Alterar a lista original, não retorna nenhum valor

print("Essa lista foi alterada com sort: ", lista)

#Para ordenar lista de maneira decrescente 
lista.sort(reverse=True)
print("Essa lista está ordenada em ordem decrescente com sort e reverse: ", lista)

#Para inverter lista, último elemento passa para o primeiro etc. Nesse caso, retornará para ordem crescente
lista.reverse()
print("Essa lista é a alterada acima e está ordenada com reverse: ", lista)