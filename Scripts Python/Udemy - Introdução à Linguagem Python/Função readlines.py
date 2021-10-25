arquivo = open("arquivo.txt") #Mostra as características do arquivo

linhas = arquivo.readlines() #Mostra o conteúdo do arquivo em uma lista


for linha in linhas:
    print(linha)