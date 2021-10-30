import random
#Com o modo random podemos chamar métodos que geram números aleatórios

#Escolha aleatória de um número de 0 a 10
numero = random.randint(0, 10)
print (numero)

#Forçar a selecionar sempre o mesmo número
random.seed(1)
numero = random.randint(0, 10)
print (numero)

