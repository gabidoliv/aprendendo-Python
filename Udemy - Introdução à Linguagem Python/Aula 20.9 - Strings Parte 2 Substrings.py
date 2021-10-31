#Buscando substrings
minha_string = "O rato roeu a roupa do rei de Roma"

busca = minha_string.find("rei") #Mostra o índice em que a palavra rei aparece
print (busca)
print (minha_string[busca:])#Todo o trecho após rei

busca2 = minha_string.find("rainha")
print(busca2)