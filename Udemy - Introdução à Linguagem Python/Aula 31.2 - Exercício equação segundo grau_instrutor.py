# Escreva um programa que resolva uma equação de segundo grau.
from math import sqrt
a = int(input("Digite o coeficiente inteiro da variável de grau 2, a =  "))
b = int(input("Digite o coeficiente inteiro da variável de grau 1, b =  "))
c = int(input("Digite o coeficiente inteiro da constante, c =  "))

delta = b**2-4*a*c
print("delta = " , delta)

raiz_delta = sqrt(delta)
print("A raiz de delta é = ", raiz_delta)

if raiz_delta < 0:
    print("Delta negativo")
else:
    x1=(-b + raiz_delta)/(2*a)
    x2=(-b - raiz_delta)/(2*a)
    print ("As raízes são", x1, "e", x2)