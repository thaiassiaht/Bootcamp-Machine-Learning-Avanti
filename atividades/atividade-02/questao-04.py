# 4. Dada uma lista de números inteiros, escreva uma função para encontrar o segundo maior valor na lista.

def encontrar_segundo_maior(lista):

    lista_unica = list(set(lista))
    if len(lista_unica) < 2:
        return None
    lista_unica.sort()
    
    return lista_unica[-2]


lista1 = [10, 5, 20, 15, 20, 2] 
print(f"Lista: {lista1} -> Segundo maior: {encontrar_segundo_maior(lista1)}")
lista2 = [5, 5, 5, 5] 
print(f"Lista: {lista2} -> Segundo maior: {encontrar_segundo_maior(lista2)}")
lista3 = [10, 2] 
print(f"Lista: {lista3} -> Segundo maior: {encontrar_segundo_maior(lista3)}")
lista4 = [10] 
print(f"Lista: {lista4} -> Segundo maior: {encontrar_segundo_maior(lista4)}")
