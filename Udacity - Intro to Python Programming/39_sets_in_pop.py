# Set permite o uso do operador in assim como listas
# Pra adicionar/remover elementos a um set, usar método pop

#Nota: Sets são desordenados, então não permite o conceito de último elemento

fruit = {"apple", "banana", "orange", "grapefruit"}  # define um set
print(fruit)

print("watermelon" in fruit)  # checa um elemento

fruit.add("watermelon")  # adiciona um elemento
print(fruit)

print(fruit.pop())  # remove um elemento aleatoriamente
print(fruit)

# Métodos de união, interseção e diferença são fáceis e mais rápidos de executar com set do que com outros contêineres