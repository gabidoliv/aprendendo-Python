# invalid dictionary - this should break
room_numbers = {
    ['Freddie', 'Jen']: 403,
    ['Ned', 'Keith']: 391,
    ['Kristin', 'Jazzmyne']: 411,
    ['Eugene', 'Zaprintch']: 395
}
print(room_numbers) # TypeError: unhashable type: 'list'

# O dicionário possui tipos de dados mutáveis para as chaves
# Em python qualquer objeto imutável (inteiro, boleano, string, tupla) é recebe um valor hash único que o identifica
# O valor hash pode ser usado pelo dicionário para rastrear chaves únicas 
# O valor hash pode ser usado pelo set para rastrear valores únicos 