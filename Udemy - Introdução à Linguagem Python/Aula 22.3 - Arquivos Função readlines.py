arquivo = open("arquivo.txt") #Mostra as características do arquivo

linhas = arquivo.readlines() #Mostra o conteúdo do arquivo em uma lista
#print (linhas) #Imprime todas as linhas na forma de lista

for linha in linhas: #Para imprimir linha por linha sem estar formatado como lista
    print(linha)