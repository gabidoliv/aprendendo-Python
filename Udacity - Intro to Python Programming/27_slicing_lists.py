sentence1 = "I wish to register a complaint." 
sentence2 = ["I", "wish", "to", "register", "a", "complaint", "."]

'''
sentence2[6]="!"
print(sentence2)

sentence2[0]= "Our Majesty"
print(sentence2)

sentence1[30]="!"
print(sentence1) #TypeError: 'str' object does not support item assignment // string = immutable
'''

sentence2[0:2] = ["We", "want"]
print(sentence2)