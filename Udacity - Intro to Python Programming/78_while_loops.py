# O laço for é um exemplo de iteração definida, ou seja, roda um quantidade predefinida de vezes
# Já o laço while é repetido uma quantidade desconhecida de vezes e finaliza quando alguma condição é alcançada

card_deck = [4,11,8,5,13,2,8,10]
hand = []

# adds the last element of the card_deck list to the hand list
# until the values in hand add up to 17 or more
while sum(hand)  < 17: # função sum - retorna a soma dos elementos na lista
    hand.append(card_deck.pop()) # função pop - método para lista que remove o último elemento e retorna o mesmo
    
print(hand)