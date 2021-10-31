# Escreva um programa que resolva uma equação de segundo grau.

a = float(input("Digite o coeficiente da variável de grau 2, a =  "))
b = float(input("Digite o coeficiente da variável de grau 1, b =  "))
c = float(input("Digite o coeficiente da variável de grau 0, c =  "))

delta = b**2-4*a*c
print("delta = " , delta)

raizdelta=delta**0.5
print("A raiz de delta é = ", raizdelta)

x1=(-b+raizdelta)/(2*a)

x2=(-b-raizdelta)/(2*a)

print("x1 é igual a ", x1)
print("x2 é igual a ", x2)