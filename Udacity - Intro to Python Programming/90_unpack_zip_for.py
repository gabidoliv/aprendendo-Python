# Pode-se dividir a dupla através de laço for

letters = ['a', 'b', 'c']
nums = [1, 2, 3]

for letter, num in zip(letters, nums):
    print("{}: {}".format(letter, num))

# unzip lista em tuplas usando asterisco

some_list = [('a', 1), ('b', 2), ('c', 3)]
print(some_list)
letters, nums = zip(*some_list)
print(letters)
print(nums)