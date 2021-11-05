#Função get_formatted_name() combina o primeiro nome e o sobrenome com um espaço entre eles
#Essa função após compor o nome completo, converte as primeiras letras em maiusculas e devolve o nome completo

def get_formatted_name(first,last):
    """Gera um nome completo formatado de modo elegante."""
    full_name = first + ' ' + last
    return full_name.title()