book_title =  ['great', 'expectations','the', 'adventures', 'of', 'sherlock','holmes','the','great','gasby','hamlet','adventures','of','huckleberry','fin']

word_counter = {} #Cria dicionário vazio

for word in book_title:
    word_counter[word] = word_counter.get(word, 0) + 1
print (word_counter)