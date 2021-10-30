meu_dicionario = {"A":"AMEIXA", "B":"BOLA","C":"CACHORRO"}

#Percorre com laço for e imprime as chaves
for chave in meu_dicionario:
    print(chave)

#Percorre com laço for e imprime os valores pra cada chave
for chave in meu_dicionario:
    print(meu_dicionario[chave])

#Percorre com laço for e imprime os valores pra cada chave e as chaves
for chave in meu_dicionario:
    print(chave+" - "+meu_dicionario[chave])