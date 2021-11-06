import unittest
from name_function import get_formatted_name

class NamesTestCase(unittest.TestCase): #herda da classe unittest.TestCase
    #Testes para 'name_function.py'

    def test_first_last_name(self): #Método que testa um aspecto de get_formatted_name()
        #Nomes como 'Janis Joplin' funcionam?
        formatted_name = get_formatted_name('janis','joplin') #Chamada da função que queremos testar (get_formatted_name) com os argumentos -> armazena o resultado em formatted_name (valor de retorno)
        self.assertEqual(formatted_name, 'Janis Joplin') # Método de asserção = "Compare o valor em formatted_name com a string 'Janis Joplin"

unittest.main()

'''
Output = 
.
----------------------------------------------------------------------
Ran 1 test in 0.001s

OK

~ O ponto na primeira linha informa que um único teste passou
~ A linha seguinte mostra que rodou 1 teste em menos de 0,001s
~ O OK informa que todos os testes de unidade do caso de teste passaram
'''