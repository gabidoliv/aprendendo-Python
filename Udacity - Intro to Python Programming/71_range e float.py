# range e float. Necessário inserir todos os argumentos no range

def frange(start,stop,step): #Define função para utilizar float com range
    i = start
    while i < stop:
        yield i
        i = round(i+step,14)

for i in frange(0.5,1.0,0.1):
    print(i)