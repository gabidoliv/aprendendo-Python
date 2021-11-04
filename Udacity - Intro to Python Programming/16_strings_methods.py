my_string = "sebastian thrun"

print(my_string.islower()) #caixa baixa = True
print(my_string.count('a')) #qnt de letras a = 2
print(my_string.find('a')) #posição = 3

print("Mohammed has {} balloons".format(27)) #Mohammed has 27 balloons

animal = "dog"
action = "bite"
print("Does your {} {}?".format(animal, action)) #Does your dog bite?

maria_string = "Maria loves {} and {}"
print(maria_string.format("math", "statistics")) #Maria loves math and statistics

# print(13.37.islower()) #islower() é um método atribuído a strings, não floats

#Método para float -> is_integer()

print(13.37.is_integer()) # False