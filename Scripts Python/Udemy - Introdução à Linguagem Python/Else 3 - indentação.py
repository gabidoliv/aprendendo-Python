#Comando condicionais - testes pra verificar se o comando deve ser realizado

a = 1
b = 5

if b > a:
    if b > 0:
        print ("b é maior que a\nb é positivo") #Cuidado com indentação
    else:
        print("b não é maior que a nem positivo")
else:
    print ("b menor que a")