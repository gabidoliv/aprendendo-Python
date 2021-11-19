'''
len () - retorna quantidade de elementos que a lista possui
max () - retorna o maior elemento da lista de acordo com o tipo de objeto da lista. Esta função é definida pelo operador > (maior que)
min () - é oposto de max()
sorted() - retorna uma cópia da lista em ordem crescente, deixando a lista original sem modificações
join () - método de string, a lista será o argumento, retorna o elemento da lista do tipo string junto de um separador determinado, por exemplo \n, - etc. 
Python segue um padrão de anexar strings, caso o join não retorne o esperado, verificar se os elementos estão separados por vírgula

append() - adiciona um elemento no final da lista
''' 
new_str = "\n".join(["fore", "aft", "starboard", "port"])
print(new_str)

name = "-".join(["García", "O'Kelly"])
print(name)