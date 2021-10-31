a = 2
b = 0

#Divisão por zero causa erro que trava a execução do programa
#Tratar excessão da divisão com palavra reservada try

try:
    print(a/b)
except:
    print("Não é permitida divisão por zero")

#Execução continua, mesmo após o erro 
print(a/a)