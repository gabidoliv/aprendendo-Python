''' Which of these lines of Python code are well formatted? 
How would you improve the readability of the codes that don't use good formatting? 
(Choose all that apply)
options:
print(((3+ 32))+ - 15//2)
print((17 - 6)%(5 + 2))
print ((1 + 2 + 4) / 13)
print(4/2 - 7*7)

'''
#option 1: 
'''print(((3+32))+ - 15//2) #27 Formatação ruim - parênteses demais, espaços extras

print((3+32) + (-15//2)) #27

print(3 + 32 + -15 // 2) #27
'''

#option 2:

print((17 - 6)%(5 + 2)) #4 Boa opção - os espacos contribuem para leitura
'''
print(17 - 6 % 5 + 2) #18
'''

#option 3:
'''
print ((1 + 2 + 4) / 13) #0.5384615384615384 Quase bom - remover os espaços extras 

print((1 + 2 + 4)/13)

'''

#option 4:

print(4/2 - 7*7) #-47.0 Boa opção
'''
print((4/2) - (7*7)) #-47.0
'''