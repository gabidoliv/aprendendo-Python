#Slicing - lembrar que o index mais baixo é inclusivo e o index mais alto é exclusivo.
list_of_random_things = [1, 3.4, 'a string', True]

print(list_of_random_things[1:2]) #3.4 - é diferente que indexar apenas 1 elemento. Os dois pontos nos dizem para ir do valor inicial à esquerda dos dois pontos, mas não incluindo o elemento à direita.

print(list_of_random_things[1:]) # Retorna final da lista = [3.4, 'a string', True]

print(list_of_random_things[:1]) #Posição zero = 1