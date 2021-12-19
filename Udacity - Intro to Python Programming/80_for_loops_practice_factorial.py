# number to find the factorial of
number = 6   

# start with our product equal to one
product = 1

# write your for loop here
for current in range(2,number+1):
    product = product * current
    print(product)  
# print the factorial of number