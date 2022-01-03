squares = [x**2 for x in range(9)] # Quadrados de inteiros até 9, sem incluir 9
print (squares)

squares = [x**2 for x in range(9) if x % 2 == 0] # Quadrados pares até 9
print (squares)
'''
squares = [x**2 for x in range(9) if x % 2 == 0 else x + 3]
print(squares) #SyntaxError: invalid syntax
'''
squares = [x**2 if x % 2 == 0 else x + 3 for x in range(9)]
print(squares)