# Tuplas podem ser utilizadas para atribuir múltiplas variáveis de maneira compacta

dimensions = 52, 40, 100 #Para tuplas, usar parênteses é opcional
length, width, height = dimensions #tuple unpacking
print("The dimensions are {} x {} x {}".format(length, width, height))

'''
# Outro modo 
length, width, height = 52, 40, 100
print("The dimensions are {} x {} x {}".format(length, width, height))
'''