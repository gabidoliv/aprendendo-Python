#Faça um programa que receba duas notas digitadas pelo usuário. Se a nota for maior ou igual a seis, escreva aprovado, senão escreva reprovado.
nota1 = float(input("Digite a nota 1: "))

nota2 = float(input("Digite a nota 2: "))

media = (nota1 +nota2)/2
print ("Sua média é = ", media)

if media >= 6.0:
    print("Parabéns, você foi aprovado")
else:
    print("Infelizmente você foi reprovado")