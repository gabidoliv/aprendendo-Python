# Escreva um programa que receba dois números e um sinal, e faça a operação matemática definida pelo sinal.

n1 = int(input("Digite o primeiro número: "))
sinal = str(input("Digite o sinal: "))
n2 = int(input("Digite o segundo número: "))

if sinal == '+':
    op = n1 + n2
elif sinal == '-':
     op = n1 - n2
elif sinal == '*':
     op = n1 * n2
elif sinal == '/':
    try:
         op = n1 / n2
    except:
        print("Não é permitida divisão por zero")
else:
    print("Sinal inválido")
print(op)