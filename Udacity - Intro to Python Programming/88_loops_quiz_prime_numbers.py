## Your code should check if each number in the list is a prime number
check_prime = [26, 39, 51, 53, 57, 79, 85]
#iterar na lista
for num in check_prime: 
    for i in range(2,num):
        #Um número não é primo se o resto de divisão é zero
        if (num % i) == 0:
            print("{} não é primo porque {} é um fator de {}".format(num,i,num))
            break
        # Caso contrário, continuar checando até buscar todos os possíveis fatores e só então, declarar como primo
        if i == num -1:
            print("{} é um número primo".format(num))