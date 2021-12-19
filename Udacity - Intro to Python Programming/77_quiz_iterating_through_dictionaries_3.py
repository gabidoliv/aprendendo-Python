# You would like to count the number of fruits in your basket. 
# In order to do this, you have the following dictionary and list of
# fruits.  Use the dictionary and list to count the total number
# of fruits and not_fruits.

fruit_count, not_fruit_count = 0, 0
basket_items = {'apples': 4, 'oranges': 19, 'kites': 3, 'sandwiches': 8}
fruits = ['apples', 'oranges', 'pears', 'peaches', 'grapes', 'bananas']

#Iterate through the dictionary
for object, count in basket_items.items():
    if object in fruits: #if the key is in the list of fruits, add to fruit_count.
        fruit_count += count
    else:
        not_fruit_count += count #if the key is not in the list, then add to the not_fruit_count

print("fruits + basket_items {} e outros valores do dicionario {} ".format(fruit_count,not_fruit_count))