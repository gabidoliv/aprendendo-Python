given_name = "William"
middle_names = "Bradley"
family_name = "Pitt"

name_length = len(given_name + " ") + len(middle_names + " ") + len(family_name) #todo: calculate how long this name is
name_length_2 = len(given_name + " " + middle_names + " " + family_name)
name_length_3 = len(given_name + middle_names + family_name) + 2

print(name_length)
print(name_length_2)
print(name_length_3)

# Now we check to make sure that the name fits within the driving license character limit
# Nothing you need to do here
driving_license_character_limit = 28
print(name_length <= driving_license_character_limit)

#Outro exemplo - len e números inteiros

print(len(835))

#Len só funciona para sequências: string, bytes, tupla, lista ou range ou
# Para coleções: dicionários, set ou frozen set