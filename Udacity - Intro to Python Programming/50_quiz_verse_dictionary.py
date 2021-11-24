verse_dict =  {'if': 3, 'you': 6, 'can': 3, 'keep': 1, 'your': 1, 'head': 1, 'when': 2, 'all': 2, 'about': 2, 'are': 1, 'losing': 1, 'theirs': 1, 'and': 3, 'blaming': 1, 'it': 1, 'on': 1, 'trust': 1, 'yourself': 1, 'men': 1, 'doubt': 1, 'but': 1, 'make': 1, 'allowance': 1, 'for': 1, 'their': 1, 'doubting': 1, 'too': 3, 'wait': 1, 'not': 1, 'be': 1, 'tired': 1, 'by': 1, 'waiting': 1, 'or': 2, 'being': 2, 'lied': 1, 'don\'t': 3, 'deal': 1, 'in': 1, 'lies': 1, 'hated': 1, 'give': 1, 'way': 1, 'to': 1, 'hating': 1, 'yet': 1, 'look': 1, 'good': 1, 'nor': 1, 'talk': 1, 'wise': 1}
print(verse_dict, '\n')

# find number of unique keys in the dictionary
num_keys = len(verse_dict.keys())
print('Number of unique keys in the dictionary: ', num_keys)

# find whether 'breathe' is a key in the dictionary
contains_breathe = verse_dict.get('breathe')
print('Is there \'breathe\' in the dictionary? ', contains_breathe)

# create and sort a list of the dictionary's keys
sorted_keys = sorted(verse_dict.keys())

# get the first element in the sorted list of keys
print('First element in the sorted list of keys: ', sorted_keys [0])

# find the element with the highest value in the list of keys
print('Element with the highest value in the list of keys: ', max(verse_dict.values())) 

#first key in verse_dict
#Dicionários não possuem ordem, não existe primeira chave. Apenas se transformar em lista
first_key = list(verse_dict.keys())[0]
print('First key in verse_dict: ', first_key)

# first element in the list created when verse_dict is sorted by keys
first_key_sorted = sorted(list(verse_dict.keys()))
print('First element in the list created when verse_dict is sorted by keys: ', first_key_sorted[0])

#key (word) with the highest value in verse_dict
print('key (word) with the highest value in verse_dict: ', max(verse_dict))