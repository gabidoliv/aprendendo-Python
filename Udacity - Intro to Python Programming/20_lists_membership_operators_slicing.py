# Slicing - usar índices para fatiar partes de um objeto (string ou lista por exemplo)

months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December'] 

q3 = months[6:9]
print(q3) # [ 'July', 'August', 'September'] 

first_half = months[:6]
print(first_half) # ['January', 'February', 'March', 'April', 'May', 'June'] 

second_half = months[6:]
print(second_half) # ['July', 'August', 'September', 'October', 'November', 'December'] 

print(len(months)) # 12 

greeting = "Hello there"
print(len(greeting)) # 11 