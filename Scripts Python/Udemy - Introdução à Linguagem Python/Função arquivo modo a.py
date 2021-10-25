w = open("arquivo.txt", 'a') #Cria arquivo. O modo a é para gravar nova linha, mantendo conteúdo pré-existente

w.write("Esse é meu arquivo. \nOlá, Mundo") #Método write para inserir conteúdo no arquivo criado

w.close() #Importante fechar o arquivo sempre que abrir -> boa prática