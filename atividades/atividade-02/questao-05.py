# 5. Crie uma função que receba uma lista de tuplas, cada uma contendo o nome e a idade de uma pessoa, e retorne a lista ordenada pelo nome das pessoas em ordem alfabética.

def ordenar_por_nome(lista_pessoas):
    
    lista_ordenada = sorted(lista_pessoas, key=lambda x: x[0])
    return lista_ordenada

pessoas = [
    ("baruc", 25),
    ("Alef", 30),
    ("Fernanda", 22),
    ("Carolina", 40)
]

resultado = ordenar_por_nome(pessoas)
print(resultado)
