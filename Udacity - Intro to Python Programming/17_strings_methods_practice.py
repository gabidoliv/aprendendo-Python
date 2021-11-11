'''
Answer the following questions about verse:

1 What is the length of the string variable verse?
2What is the index of the first occurrence of the word 'and' in verse?
3 What is the index of the last occurrence of the word 'you' in verse?
4 What is the count of occurrences of the word 'you' in the verse?

'''
# Use the appropriate functions and methods to answer the questions above
# Bonus: practice using .format() to output your answers in descriptive messages!

verse = "If you can keep your head when all about you\n  Are losing theirs and blaming it on you,\nIf you can trust yourself when all men doubt you,\n  But make allowance for their doubting too;\nIf you can wait and not be tired by waiting,\n  Or being lied about, don’t deal in lies,\nOr being hated, don’t give way to hating,\n  And yet don’t look too good, nor talk too wise:"
verse_length = len(verse)

print(verse)

print("The length of the string variable verse is: ", verse_length)
print('The length of the string variable verse is: {}'.format(verse_length))

print("The index of the first occurrence of the word 'and' in verse: ", verse.find('and'))
print("The index of the first occurrence of the word 'and' in verse: {}".format(verse.find('and')))

print("The index of the last occurrence of the word 'you' in verse: ", verse.find('you', 362))
print("The index of the last occurrence of the word 'you' in verse: {}".format(verse.find('you')))

print("The count of occurrences of the word 'you' in the verse: ", verse.count('you'))
print("The count of occurrences of the word 'you' in the verse: {}".format(verse.count('you')))