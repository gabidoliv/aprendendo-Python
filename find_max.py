'''
import math
max_num = float("-inf") #-infinito
print(max_num)
print(math.isinf(max_num)) #True
'''
import math
from find_max_function import find_max

num = float(input("\nForneça um número: "))
max = find_max(num)
print("O valor máximo é: ", max)

#Fix error: TypeError: 'float' object is not iterable