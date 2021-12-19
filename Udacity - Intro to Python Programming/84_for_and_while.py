num_list = [422, 136, 524, 85, 96, 719, 85, 92, 10, 17, 312, 542, 87, 23, 86, 191, 116, 35, 173, 45, 149, 59, 84, 69, 113, 166]

#Somar os números ímpares da lista num_list, parar no quinto número ímpar
#Não é necessário iterar pela lista toda logo, o laço while é mais apropriado
count_odd = 0
list_sum = 0
i = 0
len_num_list = len(num_list)

while (count_odd < 5) and (i < len_num_list): 
    if num_list[i] % 2 != 0: #verifica se é ímpar
        list_sum += num_list[i]
        count_odd += 1
    i += 1

print ("The numbers of odd numbers added are: {}".format(count_odd))
print ("The sum of the odd numbers added is: {}".format(list_sum))

#Se o problema fosse sobre avaliar cada item da lista se é ímpar, o laço for seria melhor