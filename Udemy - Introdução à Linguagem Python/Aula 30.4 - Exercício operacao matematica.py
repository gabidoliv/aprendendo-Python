# Escreva um programa que receba dois números e um sinal, e faça a operação matemática definida pelo sinal.

num1 = int(input("Digite um número inteiro: "))
num2 = int(input("Digite outro número inteiro: "))
sinal = str(input("\n+ para soma \n- para subtração\n/ para divisão\n* para multiplicação\nDigite o sinal da operação matemática: "))
print(sinal)

def soma(num1, num2):
    return num1+num2

def multiplicação(num1, num2):
    return num1+num2

def subtracao(num1, num2):
    return num1-num2

def multicacao(num1, num2):
    return num1*num2

def divisao(num1, num2):
    return num1/num2   

if sinal == '+':
    print (soma(num1,num2))
if sinal == '-':
    print(subtracao(num1,num2))
if sinal == '*':
    print(multicacao(num1,num2))
if sinal == '/':
    try:
        print(divisao(num1,num2))
    except:
        print("Não é permitida divisão por zero")
else:
    print("Sinal inválido")