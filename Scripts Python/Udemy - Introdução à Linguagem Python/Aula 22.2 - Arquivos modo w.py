w = open("arquivo.txt", 'w') #Cria arquivo. O modo w é para sobrescrever arquivo já existente

w.write("Esse é meu arquivo. \nOlá, Mundo") #Método write para inserir conteúdo no arquivo criado

w.close() #Importante fechar o arquivo sempre que abrir -> boa prática