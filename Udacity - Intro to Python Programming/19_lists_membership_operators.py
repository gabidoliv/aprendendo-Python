list_of_random_things = [1, 3.4, 'a string', True]


print(list_of_random_things[0])

print(len(list_of_random_things))

# print(list_of_random_things[len(list_of_random_things)]) #IndexError: list index out of range

print(list_of_random_things[len(list_of_random_things) - 1]) #Recupera o último elemento da lista

#Usando sinal negativo para indexar do final da lista

print(list_of_random_things[-1]) #Último elemento da lista
print(list_of_random_things[-2]) #Penúltimo elemento da lista