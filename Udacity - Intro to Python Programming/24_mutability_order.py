#Strings não são mutáveis

greeting = "Hello there"
print(greeting)
greeting [0] = 'M'
print(greeting) #TypeError: 'str' object does not support item assignment