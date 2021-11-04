#Strings podem ser definidas por aspas simples ou duplas
#A convenção é definir variável string com aspa duplas, salvo exceções como o exemplo abaixo

#Outro detalhe: Barra invertida para apóstrofo
salesman = '"I think you\'re an encyclopaedia salesman"'
print(salesman)

#Operadores para strings: + para concatenar, * para repetir
first_word = "Hello"
second_word = "There"

print(first_word + " " + second_word)

word = "Hello"
print (word * 5)

udacity_length = len("Udacity") #len e print são funções built-in - formam ação utilizando o valor entre parênteses
print(udacity_length)

#A diferença entre len e print é que len retorna um valor que pode ser armazenado em uma variável
#Built-in significa que Python fornece a função
print(len(first_word))

# index para strings
print(first_word[0])
print(first_word[1])

print(len("ababa"))
print(len("ab"))

print(len("ababa") / len("ab") ) #Como len retorna um inteiro, é possível fazer divisão