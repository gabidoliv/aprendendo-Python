house_number = 13
street_name = "The Crescent"
town_home = "Belmont"
print(type(house_number)) # <class 'int'>

address = str(house_number) + " " + street_name + ", " + town_home
print(address) # 13 The Crescent, Belmont
print(type(address)) # <class 'str'>

print(len("my_string")) #9
print(type(len("my_string"))) #<class 'int'>
print(type("hippo" *12)) #<class 'str'>

print("0" + "5") #05
print("0" + "5") #05
print("0" + 5) #erro <module>
print(0 + "5") #erro "can only concatenate str (not 'int') to str"