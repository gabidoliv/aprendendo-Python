# list comprehension

x = [1,2,3,4,5]
# y = [valor_a_adicionar laço condição] 
y = [i**2 for i in x] #Exemplo sem condição
z = [i for i in x if i%2==1] #Condição = números ímpares da lista x, %2==1, resto de divisão por 2 é sempre 1 para números impares

print("Usando list comprehension")
print(x)
print(y)
print(z)