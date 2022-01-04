book_title =  ['great', 'expectations','the', 'adventures', 'of', 'sherlock','holmes','the','great','gasby','hamlet','adventures','of','huckleberry','fin']

word_counter = {} #Cria dicionário vazio

for word in book_title:
    if word not in word_counter:
        word_counter[word] = 1 # Se não existe, seu valor passa a ser 1 
    else:
        word_counter[word] += 1 # Se já existe o elemento na lista soma 1 ao valor dele
print (word_counter)